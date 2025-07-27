from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty



class ClickerLayout(BoxLayout):
    clicks = NumericProperty(0)
    to_click = 1
    upgrade_cost = NumericProperty(150)

    def on_button_click(self):
        self.clicks += self.to_click
    def reset(self):
    	self.clicks = 0
    	self.upgrade_cost = 150
    	self.to_click = 1
    def upgrade(self):
    	if self.clicks >= self.upgrade_cost:
    		self.clicks -= self.upgrade_cost
    		self.upgrade_cost += 100
    		self.to_click += 1

class ClickerApp(App):
    def build(self):
        return ClickerLayout()

if __name__ == "__main__":
    ClickerApp().run()