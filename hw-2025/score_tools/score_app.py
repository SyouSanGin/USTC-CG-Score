from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Label, Button,Switch,Input,Static, Log
from textual.validation import Number
from textual.containers import VerticalScroll, HorizontalGroup, Horizontal,Vertical,VerticalGroup
from textual.reactive import reactive
from textual import on
import score_tools.score_group as score_group


class CusSwitch(Switch):
    def __init__(self, value = False, *, animate = True, name = None, id = None, classes = None, disabled = False, tooltip = None, 
                 grp: score_group.FixedLeafGroup = None):
        self.grp = grp
        super().__init__(value, animate=animate, name=name, id=id, classes=classes, disabled=disabled, tooltip=tooltip)
    def watch_value(self, value):
        super().watch_value(value)
        self.grp.set_status(value)
    
class FixedScoreBox(HorizontalGroup):
    def __init__(self, *children, name = None, id = None, classes = None, disabled = False, markup = True,
                 grp: score_group.FixedLeafGroup=None):
        self.grp =grp
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)
        
    def compose(self):
        yield HorizontalGroup(Label("{} ({})".format(self.grp.get_desc(), self.grp.get_full())), CusSwitch(value=self.grp.get_status(),grp=self.grp))
        
class CusInput(Input):
    def __init__(self, value = None, placeholder = "", highlighter = None, password = False, *, restrict = None, type = "text", max_length = 0, suggester = None, validators = None, validate_on = None, valid_empty = False, select_on_focus = True, name = None, id = None, classes = None, disabled = False, tooltip = None,
                 grp : score_group.MutableLeafGroup=None):
        self.grp = grp
        super().__init__(value=str(grp.get_score()), type="number",validators=[Number(grp.get_range()[0], grp.get_range()[1], "Our of range! {}".format(grp.get_range()))], validate_on=validate_on, valid_empty=False, select_on_focus=select_on_focus, name=name, id=id, classes=classes, disabled=disabled, tooltip=tooltip)        
        
    def watch_value(self, val):
        minimum, maximum = self.grp.get_range()
        try: # to float
            if len(val) > 0 and  minimum <= float(val) and maximum >= float(val):
                self.grp.set_score(float(val)) 
        except:
            pass

class MutableScoreBox(HorizontalGroup):
    def __init__(self, *children, name = None, id = None, classes = None, disabled = False, markup = True,
                 grp:score_group.MutableLeafGroup=None):
        self.grp = grp
        super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)
    def compose(self):
        m,M = self.grp.get_range()
        yield HorizontalGroup(Label("{} ({} => {})".format(self.grp.get_desc(),m,M )), CusInput(grp=self.grp))
    
    
class Scoring(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("q", "quit", "Quit the app")]
    def __init__(self, driver_class = None, css_path = None, watch_css = False, ansi_color = False, grp: score_group.ScoreGroup = None, addon: str = ""):
        self.grp = grp
        self.addon = addon
        super().__init__(driver_class, css_path, watch_css, ansi_color)
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        # create score items
        res =  Scoring.my_create_widgets(self.grp)
        btn = Button("Create report", id='btn')
        btn_pop = Button("Create report (External)", id='btnex')
        self.logger = Log()
        # yield VerticalScroll(res, btn, self.logger)
        yield VerticalScroll(res, VerticalGroup(HorizontalGroup(btn,btn_pop), self.logger))

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    def action_quit(self):
        return super().action_quit()
    
    @on(Button.Pressed, "#btn")
    def handle_btn(self):
        self.logger.clear()
        self.logger.write_line(score_group.generate_report(self.grp,self.addon))
        
    @on(Button.Pressed, "#btnex")
    def handle_btnex(self):
        report_text = score_group.generate_report(self.grp,self.addon)
        with open(".report.txt", 'w', encoding='utf-8') as f:
            f.write(report_text)
    
    @staticmethod
    def my_create_widgets(grp:score_group.ScoreGroup, dep=0):
        if isinstance(grp, score_group.FixedLeafGroup):
            return HorizontalGroup(Label("    "*dep),FixedScoreBox(grp=grp))
        elif isinstance(grp, score_group.MutableLeafGroup):
            return HorizontalGroup(Label("    "*dep), MutableScoreBox(grp=grp))
        elif isinstance(grp, score_group.MercifulLeafGroup):
            return HorizontalGroup(Label("    "*dep), FixedScoreBox(grp=grp))
        else:
            vals = [Scoring.my_create_widgets(i, dep+1) for i in grp.subgroups]
            return VerticalGroup(
                Label("    "*dep + "{}".format(grp.get_desc())),*vals
            )
            
            
def run_group(grp : score_group.ScoreGroup,addon: str = ""):
    app=Scoring(grp=grp,addon=addon)
    app.run()

if __name__ == "__main__":
    
    g0 = score_group.FixedLeafGroup(score=114, status=True)
    g1 = score_group.MutableLeafGroup(initial=1)
    g2 = score_group.AddGroup(subgroups=[g0,g1]*1)
    g3 = score_group.MutableLeafGroup(initial=12, desc="Damn", score_max=113415)
    g4 = score_group.AverageGroup(desc="Ave", subgroups=[g3,g2])
    
    
    
    app = Scoring(grp=g4)
    app.run()
    # print(score_group.generate_report(g2))
    # print(g2.get_desc())