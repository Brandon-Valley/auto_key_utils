import keyboard as k
from pynput.keyboard import Key
from pynput.keyboard import Controller
from pynput.keyboard import Listener
import time
import _tkinter
from pynput import keyboard
from func_timeout import func_timeout, FunctionTimedOut


if __name__ == "__main__": 
    from   usms.clipboard_utils import clipboard_utils as cu
else:
    from . usms.clipboard_utils import clipboard_utils as cu



''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        Selections
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''

def make_selection(select_mode, num_arrows = None):
    def shift_home_select():
        keyboard = Controller()
        with keyboard.pressed(Key.shift):
            keyboard.press(Key.home)
            keyboard.release(Key.shift)
    
    if select_mode == 'all':
        k.press_and_release('Ctrl+a')
        
    elif select_mode == 'shift_home':            
        shift_home_select()
        
    elif select_mode == 'end_shift_home':
        k.press_and_release('end')
        shift_home_select()
        
    elif select_mode == 'end_shift_left_arrow':
        k.press_and_release('end')
        keyboard = Controller()
        keyboard.press(Key.shift)
        
        for x in range(num_arrows):
            keyboard.press(Key.left)
            keyboard.release(Key.left)

        keyboard.release(Key.shift)
        


# Ctrl + a, copy to clipboard, return clipboard
def get_selection(deselect_key_str = None, error_on_empty_clipboard = False):
    
    try:
        og_clipboard = cu.get_clipboard()
    except(_tkinter.TclError):
        og_clipboard = ''
        
        
    cu.clear_clipboard()
    
    k.press_and_release('Ctrl+c')    
    
    time.sleep(.3)
    
    new_clipboard = cu.get_clipboard()
    
    if error_on_empty_clipboard and str(new_clipboard) == '':
        raise Exception("ERROR:  Tried to copy current selection, nothing was copied to clipboard")
        
    
    cu.set_clipboard(og_clipboard)
    
    if deselect_key_str != None:
        time.sleep(.3)# need ??????????????????????????????????????????????????????
        k.press_and_release(deselect_key_str)
    
    return new_clipboard


# not tested
def make_then_get_selection(select_mode, deselect_key_str = None, error_on_empty_clipboard = False, num_arrows = None):
    make_selection(select_mode, num_arrows)
    time.sleep(.3)
    return get_selection(deselect_key_str, error_on_empty_clipboard)


''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        Clipboard
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''

def paste_preserve_clipboard(to_paste):
    og_cb = cu.get_clipboard()
    cu.set_clipboard(to_paste)
    k.press_and_release('ctrl+v')
    cu.set_clipboard(og_cb)


''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        Keyboard
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''



    
    
    
def wait_until_first_release():
    def on_press(key):
        pass
     
    def on_release(key):
        return False
     
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()    
    
    
    
    
    
    

if __name__ == '__main__':
    print('In Main:  auto_key_utils')
    time.sleep(2)
    wait_until_first_release()
#     any_key_pressed()
#     from getkey import getkey, keys
#     print('getting keys')
#     key = getkey(blocking = False)
#     print('key: ', key)
#     print('key: ', key.name)
#     
    
#     import ctypes
#     
# #     win32api.G
# #     print(ctypes.Get)
#     
#     print(ctypes.windll.user32.GetKeyboardState(1))
    
#     time.sleep(2)
    
#     wait_until_no_keys_pressed()
#     print(show_poll_keyboard())
#     print(get_keyboard_input())
    
    
    
# # #     print(get_select_all())
#     time.sleep(3)
# #     k.press_and_release('shift+home')
# # #     k.press_and_release('home')
# 
# 
# #     make_selection('end_shift_left_arrow', num_arrows=3)
#     
#     
#     print(make_then_get_selection('end_shift_left_arrow', num_arrows = 3))
# #     make_selection('end_shift_home', num_arrows=3)
# 
# #     k.press('shift')
# #     time.sleep(.3)
# #     k.press_and_release('left arrow')
# #     time.sleep(.3)
# # 
# #     k.press_and_release('left arrow')
# #     time.sleep(.3)
# #     k.press_and_release('left arrow')
# #     time.sleep(.3)
# #     k.release('shift')
#     
#     
#     k.release('shift')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print('End of Main:  auto_key_utils')