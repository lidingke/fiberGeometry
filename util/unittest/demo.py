from time import sleep

from util.unittest.knife import Knife
# from util.unittest.gui import View

# print main()
def knife_into(view_instance):
    knife = Knife(view_instance)
    view_instance.input_line.setText("123")
    knife.enter_button.clicked()
    sleep(1)
    text = view_instance.output_line.text()
    assert text == "124"
    sleep(1)
    view_instance.input_line.setText("1234")
    sleep(1)
    knife.enter_button.clicked()
    text = view_instance.output_line.text()
    assert text == "1235"
    sleep(1)
    view_instance.close()
