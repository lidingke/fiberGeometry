#coding:utf-8
import pdb
from time import sleep

from util.unittest.knife import Knife
# from util.unittest.gui import View

# print main()
def knife_into_demo(view_instance):
    # sleep()
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
    sleep(3)
    view_instance.close()

def knife_into_main(view_instance):
    knife = Knife(view_instance)
    sleep(1)
    print dir(knife._view)
    # view_instance.input_line.setText("123")
    knife._view.beginTestCV.clicked()

    sleep(10)
    text = view_instance._view.resultShowCV.toPlainText()
    # pdb.set_trace()
    print unicode(text)
    # knife._modecv.light_controller.emit_light_ready()
    # assert text == "124"
    # sleep(1)
    # view_instance.input_line.setText("1234")
    # sleep(1)
    # knife.enter_button.clicked()
    # text = view_instance.output_line.text()
    # assert text == "1235"
    # sleep(1)
    # view_instance.close()

def test_knife_into_main(view_instance):
    knife = Knife(view_instance)
    knife.view.target_button.clicked()
    sleep(10)
    text = view_instance._view.show_plain.toPlainText()
    assert unicode(text) == "target"

