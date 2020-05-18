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



def make_then_get_selection(select_mode, deselect_key_str = None, error_on_empty_clipboard = False, num_arrows = None):
    make_selection(select_mode, num_arrows)
    time.sleep(.3)
    return get_selection(deselect_key_str, error_on_empty_clipboard)



''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        Keyboard
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''




# def show_poll_keyboard():
#     ''' 
#         This func is not used for anything
#         It's just a really good example of how to poll the keyboard
#         Just here for future reference
#     '''
#     def on_press(key):
#         print('{0} pressed'.format(
#             key))
#     
#     def on_release(key):
#         print('{0} release'.format(
#             key))
#         if key == Key.esc:
#             # Stop listener
#             return False
#     
#     # Collect events until released
#     with Listener(
#             on_press=on_press,
#             on_release=on_release) as listener:
#         listener.join()

import keyboard as just_keyboard

def any_key_pressed(timeout = 0.1):
    keys_pressed = set()
#     def wait_for_key_pressed():
    def on_press(key):
        
#         keys_pressed.append('{0} pressed'.format(key))
#         keys_pressed.add(key)


        raw = ('{}'.format(key))
        print('raw: ', raw, type(raw))
        keys_pressed.add(raw)

        keys_pressed.add(('{}'.format(key).replace('"', '')))
        print('key pressed')
#         return False
     
    def on_release(key):
#         keys_pressed.append('{0} released'.format(key))
#         keys_pressed.remove(key)
        keys_pressed.remove(('{0}'.format(key)))
#         return False
 
     
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    
    print('before Start')
    
    from threading import Thread
    
    thread = Thread(target = listener.start)
    thread.start()
    print('past thread start')
    

    


    time.sleep(.1)
    
    
    while(len(keys_pressed) > 0):
        keys_to_remove = []
        print('keys still pressed: ', keys_pressed)
        for key in keys_pressed:
            print('                      double checking if key still down: ', key, type(key), just_keyboard.is_pressed(key.replace("'", '')))
            if not just_keyboard.is_pressed(key.replace("'", '')):
                print('                                                                    removing by doubble check')
                keys_to_remove.append(key)
#                 keys_pressed.remove(key)

        for key in keys_to_remove:
            keys_pressed.remove(key)
        
    
    
    listener.stop()
    thread.join()
    print('after thread end')

    return

#     print(keys_pressed)
#     if len(keys_pressed) > 0:
#         return True
#     return False
        
#         return 'NO KEYS PRESSED'


#     print(wait_for_key_pressed())
#     print(keys_pressed)

#     try:
#         doitReturnValue = func_timeout(timeout, wait_for_key_pressed)
#         print('doitReturnValue:  ', doitReturnValue)
#         return True
#      
#     except FunctionTimedOut:
#         return False
#      
#     except Exception as e:
#         raise
#     
    
def wait_until_no_keys_pressed():
#     while(any_key_pressed() == True):
#         pass


    while(True):
        print('any_key_pressed(): ' , any_key_pressed())


#     while(True):
#         if any_key_pressed() == False:
#             
#             
#             if any_key_pressed() == False:
#                 return

#     return
    
    
    

if __name__ == '__main__':
    print('In Main:  auto_key_utils')
    time.sleep(2)
    any_key_pressed()
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