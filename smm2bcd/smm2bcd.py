import sys, os, os.path, tkinter
from tkinter import filedialog, messagebox


def open_enc_course():
    global dec_course_path
    home = os.path.expanduser("~")
    root = tkinter.Tk()
    root.withdraw()
    course_path = filedialog.askopenfilename(initialdir = home + "/Desktop",title = "Select An Encrypted Super Mario Maker 2 Course Data File",filetypes = (("Binary Course Data Files","*.bcd"),("All Files","*.*")))
    if course_path:
        head, tail = os.path.split(course_path)
        dec_course_path = head + '/dec_' + tail
        with open('path_files/decryptor_path.txt','r') as decryptor_path:
            dec_path = decryptor_path.read()
            os.system(dec_path + ' ' + course_path + ' ' + dec_course_path)
            print(course_path)
    else:
        print('You Chose Nothing!')


def import_enc_course_path():
    global dec_course_path
    with open('path_files/enc_course_path.txt','r') as course_path:
        enc_course_path = course_path.read()
        head, tail = os.path.split(enc_course_path)
        dec_course_path = head + '/dec_' + tail
        with open('path_files/decryptor_path.txt','r') as decryptor_path:
            dec_path = decryptor_path.read()
            os.system(dec_path + ' ' + enc_course_path + ' ' + dec_course_path)
            print(dec_course_path)


def open_dec_course():
    global dec_course_path
    home = os.path.expanduser("~")
    root = tkinter.Tk()
    root.withdraw()
    dec_course_path = filedialog.askopenfilename(initialdir = home + "/Desktop",title = "Select A Decrypted Super Mario Maker 2 Course Data File",filetypes = (("Binary Course Data Files","*.bcd"),("All Files","*.*")))
    if dec_course_path:
        print(dec_course_path)
    else:
        print('You Chose Nothing!')


def import_dec_course_path():
    global dec_course_path
    with open('path_files/dec_course_path.txt','r') as course_path:
        dec_course_path = course_path.read()
        print(dec_course_path)


def read_main_attributes():
    global dec_course_path
    with open(dec_course_path,'rb') as course:
        for i in range(2600):
            course.seek(596 + 32 * i)
            entity_attribute = course.read(1)
            integer = int.from_bytes(entity_attribute, byteorder='big')
            hexadecimal = hex(integer)
            high, low = int(hexadecimal, 16) >> 4, int(hexadecimal, 16) & 0x0F
            high = hex(high)
            low = hex(low)
            if low == '0x0' or low == '0x8':
                status = 'Regular'
            if low == '0x1' or low == '0x9':
                status = 'In A Pipe'
            if low == '0x2' or low == '0xA':
                status = 'Winged'
            if low == '0x3' or low == '0xB':
                status = 'In Pipe And Winged'
            if low == '0x4' or low == '0xC':
                status = 'Shaken'
            if low == '0x5' or low == '0xD':
                status = 'Shaken In A Pipe'
            if low == '0x6' or low == '0xE':
                status = 'Shaken And Winged'
            if low == '0x7' or low == '0xF':
                status = 'Shaken And In Pipe And Winged'
            if high == '0x0' or high == '0x1' or high == '0x8' or high == '0x9':
                rotation = 'Right Facing'
            if high == '0x2' or high == '0x3' or high == '0xA' or high == '0xB':
                rotation = 'Left Facing'
            if high == '0x4' or high == '0x5' or high == '0xC' or high == '0xD':
                rotation = 'Upward Facing'
            if high == '0x6' or high == '0x7' or high == '0xE' or high == '0xF':
                rotation = 'Downward Facing'
            print(status + ', ' + rotation + ' Entity ' + str(i) + ': ' + str(high) + ' ' + str(low) + ' @' + str(hex(628 + 32 * i)))


def read_secondary_attributes():
    global dec_course_path
    with open(dec_course_path,'rb') as course:
        for i in range(2600):
            course.seek(596 + 32 * i)
            entity_attribute = course.read(1)
            integer = int.from_bytes(entity_attribute, byteorder='big')
            hexadecimal = hex(integer)
            high, low = int(hexadecimal, 16) >> 4, int(hexadecimal, 16) & 0x0F
            high = hex(high)
            low = hex(low)
            if low == '0x0' or low == '0x8':
                status = 'Regular'
            if low == '0x1' or low == '0x9':
                status = 'In A Pipe'
            if low == '0x2' or low == '0xA':
                status = 'Winged'
            if low == '0x3' or low == '0xB':
                status = 'In Pipe And Winged'
            if low == '0x4' or low == '0xC':
                status = 'Shaken'
            if low == '0x5' or low == '0xD':
                status = 'Shaken In A Pipe'
            if low == '0x6' or low == '0xE':
                status = 'Shaken And Winged'
            if low == '0x7' or low == '0xF':
                status = 'Shaken And In Pipe And Winged'
            if high == '0x0' or high == '0x1' or high == '0x8' or high == '0x9':
                rotation = 'Right Facing'
            if high == '0x2' or high == '0x3' or high == '0xA' or high == '0xB':
                rotation = 'Left Facing'
            if high == '0x4' or high == '0x5' or high == '0xC' or high == '0xD':
                rotation = 'Upward Facing'
            if high == '0x6' or high == '0x7' or high == '0xE' or high == '0xF':
                rotation = 'Downward Facing'
            print(status + ', ' + rotation + ' Entity ' + str(i) + ': ' + str(high) + ' ' + str(low) + ' @' + str(hex(628 + 32 * i)))


def check_key_status():
    global dec_course_path
    with open(dec_course_path,'rb') as course:
        for i in range(2600):
            course.seek(609 + 32 * i)
            x = course.read(1)
            key_status = f'Unknown({x})'
            if x == bytes([0x00]):
                key_status = 'Does Not Have Key'
            if x == bytes([0x12]):
                key_status = 'Does Have Key'
            print('Entity ' + str(i) + ' @' + str(hex(628 + 32 * i)) + ' ' + key_status)


def read_entities():
    global dec_course_path
    with open(dec_course_path,'rb') as course:
        for i in range(2600):
            course.seek(608 + 32 * i)
            entity_id = course.read(3)
            entity_name = f'Unknown({entity_id})'
            if entity_id == bytes([0x00, 0x00, 0xFF]) or entity_id == bytes([0x00, 0x12, 0xFF]):
                entity_name = 'Goomba/Galoomba'
            if entity_id == bytes([0x01, 0x00, 0xFF]) or entity_id == bytes([0x01, 0x12, 0xFF]):
                entity_name = 'Koopa Troopa'
            if entity_id == bytes([0x02, 0x00, 0xFF]) or entity_id == bytes([0x02, 0x12, 0xFF]):
                entity_name = 'Piranha Plant/Jumping Piranha Plant'
            if entity_id == bytes([0x03, 0x00, 0xFF]) or entity_id == bytes([0x03, 0x12, 0xFF]):
                entity_name = 'Hammer Bro'
            if entity_id == bytes([0x04, 0x00, 0xFF]) or entity_id == bytes([0x04, 0x12, 0xFF]):
                entity_name = 'Block'
            if entity_id == bytes([0x05, 0x00, 0xFF]) or entity_id == bytes([0x05, 0x12, 0xFF]):
                entity_name = '? Block'
            if entity_id == bytes([0x06, 0x00, 0xFF]) or entity_id == bytes([0x06, 0x12, 0xFF]):
                entity_name = 'Hard Block'
            if entity_id == bytes([0x07, 0x00, 0xFF]) or entity_id == bytes([0x07, 0x12, 0xFF]):
                entity_name = 'Ground'
            if entity_id == bytes([0x08, 0x00, 0xFF]) or entity_id == bytes([0x08, 0x12, 0xFF]):
                entity_name = 'Coin'
            if entity_id == bytes([0x09, 0x00, 0xFF]) or entity_id == bytes([0x09, 0x12, 0xFF]):
                entity_name = 'Pipe'
            if entity_id == bytes([0x0A, 0x00, 0xFF]) or entity_id == bytes([0x0A, 0x12, 0xFF]):
                entity_name = 'Trampoline'
            if entity_id == bytes([0x0B, 0x00, 0xFF]) or entity_id == bytes([0x0B, 0x12, 0xFF]):
                entity_name = 'Lift/Cloud Lift'
            if entity_id == bytes([0x0C, 0x00, 0xFF]) or entity_id == bytes([0x0C, 0x12, 0xFF]):
                entity_name = 'Thwomp'
            if entity_id == bytes([0x0D, 0x00, 0xFF]) or entity_id == bytes([0x0D, 0x12, 0xFF]):
                entity_name = 'Bill Blaster'
            if entity_id == bytes([0x0E, 0x00, 0xFF]) or entity_id == bytes([0x0E, 0x12, 0xFF]):
                entity_name = 'Mushroom Platform'
            if entity_id == bytes([0x0F, 0x00, 0xFF]) or entity_id == bytes([0x0F, 0x12, 0xFF]):
                entity_name = 'Bob-omb'
            if entity_id == bytes([0x10, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                entity_name = 'Semisolid Platform'
            if entity_id == bytes([0x11, 0x00, 0xFF]) or entity_id == bytes([0x11, 0x12, 0xFF]):
                entity_name = 'Bridge'
            if entity_id == bytes([0x12, 0x00, 0xFF]) or entity_id == bytes([0x12, 0x12, 0xFF]):
                entity_name = 'P-Switch'
            if entity_id == bytes([0x13, 0x00, 0xFF]) or entity_id == bytes([0x13, 0x12, 0xFF]):
                entity_name = 'Pow Block'
            if entity_id == bytes([0x14, 0x00, 0xFF]) or entity_id == bytes([0x14, 0x12, 0xFF]):
                entity_name = 'Super Mushroom'
            if entity_id == bytes([0x15, 0x00, 0xFF]) or entity_id == bytes([0x15, 0x12, 0xFF]):
                entity_name = 'Donut Block'
            if entity_id == bytes([0x16, 0x00, 0xFF]) or entity_id == bytes([0x16, 0x12, 0xFF]):
                entity_name = 'Cloud Block'
            if entity_id == bytes([0x17, 0x00, 0xFF]) or entity_id == bytes([0x17, 0x12, 0xFF]):
                entity_name = 'Note Block'
            if entity_id == bytes([0x18, 0x00, 0xFF]) or entity_id == bytes([0x18, 0x12, 0xFF]):
                entity_name = 'Firebar'
            if entity_id == bytes([0x19, 0x00, 0xFF]) or entity_id == bytes([0x19, 0x12, 0xFF]):
                entity_name = 'Spiny'
            if entity_id == bytes([0x1A, 0x00, 0xFF]) or entity_id == bytes([0x1A, 0x12, 0xFF]):
                entity_name = 'Goal Ground'
            if entity_id == bytes([0x1B, 0x00, 0xFF]) or entity_id == bytes([0x1B, 0x12, 0xFF]):
                entity_name = 'Goal Pole'
            if entity_id == bytes([0x1C, 0x00, 0xFF]) or entity_id == bytes([0x1C, 0x12, 0xFF]):
                entity_name = 'Buzzy Beatle'
            if entity_id == bytes([0x1D, 0x00, 0xFF]) or entity_id == bytes([0x1D, 0x12, 0xFF]):
                entity_name = 'Hidden Block'
            if entity_id == bytes([0x1E, 0x00, 0xFF]) or entity_id == bytes([0x1E, 0x12, 0xFF]):
                entity_name = 'Lakitu'
            if entity_id == bytes([0x1F, 0x00, 0xFF]) or entity_id == bytes([0x1F, 0x12, 0xFF]):
                entity_name = 'Cloud'
            if entity_id == bytes([0x20, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                entity_name = 'Banzai Bill'
            if entity_id == bytes([0x21, 0x00, 0xFF]) or entity_id == bytes([0x21, 0x12, 0xFF]):
                entity_name = '1-Up Mushroom'
            if entity_id == bytes([0x22, 0x00, 0xFF]) or entity_id == bytes([0x22, 0x12, 0xFF]):
                entity_name = 'Fire Flower'
            if entity_id == bytes([0x23, 0x00, 0xFF]) or entity_id == bytes([0x23, 0x12, 0xFF]):
                entity_name = 'Super Star'
            if entity_id == bytes([0x24, 0x00, 0xFF]) or entity_id == bytes([0x24, 0x12, 0xFF]):
                entity_name = 'Lava Lift'
            if entity_id == bytes([0x25, 0x00, 0xFF]) or entity_id == bytes([0x25, 0x12, 0xFF]):
                entity_name = 'Ground Start'
            if entity_id == bytes([0x26, 0x00, 0xFF]) or entity_id == bytes([0x26, 0x12, 0xFF]):
                entity_name = 'Start Arrow'
            if entity_id == bytes([0x27, 0x00, 0xFF]) or entity_id == bytes([0x27, 0x12, 0xFF]):
                entity_name = 'Kameck'
            if entity_id == bytes([0x28, 0x00, 0xFF]) or entity_id == bytes([0x28, 0x12, 0xFF]):
                entity_name = 'Spike Top'
            if entity_id == bytes([0x29, 0x00, 0xFF]) or entity_id == bytes([0x29, 0x12, 0xFF]):
                entity_name = 'Boo'
            if entity_id == bytes([0x2A, 0x00, 0xFF]) or entity_id == bytes([0x2A, 0x12, 0xFF]):
                entity_name = 'Koopa Clown Car'
            if entity_id == bytes([0x2B, 0x00, 0xFF]) or entity_id == bytes([0x2B, 0x12, 0xFF]):
                entity_name = 'Spike Trap'
            if entity_id == bytes([0x2C, 0x00, 0xFF]) or entity_id == bytes([0x2C, 0x12, 0xFF]):
                entity_name = '3rd Tier Powerup'
            if entity_id == bytes([0x2D, 0x00, 0xFF]) or entity_id == bytes([0x2D, 0x12, 0xFF]):
                entity_name = 'Shoe Goomba/Yoshi'
            if entity_id == bytes([0x2E, 0x00, 0xFF]) or entity_id == bytes([0x2E, 0x12, 0xFF]):
                entity_name = 'Dry Bones'
            if entity_id == bytes([0x2F, 0x00, 0xFF]) or entity_id == bytes([0x2F, 0x12, 0xFF]):
                entity_name = 'Cannon'
            if entity_id == bytes([0x30, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                entity_name = 'Blooper'
            if entity_id == bytes([0x31, 0x00, 0xFF]) or entity_id == bytes([0x31, 0x12, 0xFF]):
                entity_name = 'Castle Bridge'
            if entity_id == bytes([0x32, 0x00, 0xFF]) or entity_id == bytes([0x32, 0x12, 0xFF]):
                entity_name = 'Hop-Chops'
            if entity_id == bytes([0x33, 0x00, 0xFF]) or entity_id == bytes([0x33, 0x12, 0xFF]):
                entity_name = 'Skipsqueak'
            if entity_id == bytes([0x34, 0x00, 0xFF]) or entity_id == bytes([0x34, 0x12, 0xFF]):
                entity_name = 'Wiggler'
            if entity_id == bytes([0x35, 0x00, 0xFF]) or entity_id == bytes([0x35, 0x12, 0xFF]):
                entity_name = 'Conveyer Belt'
            if entity_id == bytes([0x36, 0x00, 0xFF]) or entity_id == bytes([0x36, 0x12, 0xFF]):
                entity_name = 'Burner'
            if entity_id == bytes([0x37, 0x00, 0xFF]) or entity_id == bytes([0x37, 0x12, 0xFF]):
                entity_name = 'Warp Door'
            if entity_id == bytes([0x38, 0x00, 0xFF]) or entity_id == bytes([0x38, 0x12, 0xFF]):
                entity_name = 'Cheep Cheep'
            if entity_id == bytes([0x39, 0x00, 0xFF]) or entity_id == bytes([0x39, 0x12, 0xFF]):
                entity_name = 'Muncher'
            if entity_id == bytes([0x3A, 0x00, 0xFF]) or entity_id == bytes([0x3A, 0x12, 0xFF]):
                entity_name = 'Rocky Wrench'
            if entity_id == bytes([0x3B, 0x00, 0xFF]) or entity_id == bytes([0x3B, 0x12, 0xFF]):
                entity_name = 'Rail'
            if entity_id == bytes([0x3C, 0x00, 0xFF]) or entity_id == bytes([0x3C, 0x12, 0xFF]):
                entity_name = 'Lava Bubble'
            if entity_id == bytes([0x3D, 0x00, 0xFF]) or entity_id == bytes([0x3D, 0x12, 0xFF]):
                entity_name = 'Chain Chomp'
            if entity_id == bytes([0x3E, 0x00, 0xFF]) or entity_id == bytes([0x3E, 0x12, 0xFF]):
                entity_name = 'Bowser/Meowser'
            if entity_id == bytes([0x3F, 0x00, 0xFF]) or entity_id == bytes([0x3F, 0x12, 0xFF]):
                entity_name = 'Ice Block'
            if entity_id == bytes([0x40, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                entity_name = 'Vine'
            if entity_id == bytes([0x41, 0x00, 0xFF]) or entity_id == bytes([0x41, 0x12, 0xFF]):
                entity_name = 'Stingby'
            if entity_id == bytes([0x42, 0x00, 0xFF]) or entity_id == bytes([0x42, 0x12, 0xFF]):
                entity_name = 'Arrow Sign'
            if entity_id == bytes([0x43, 0x00, 0xFF]) or entity_id == bytes([0x43, 0x12, 0xFF]):
                entity_name = 'One-Way Wall'
            if entity_id == bytes([0x44, 0x00, 0xFF]) or entity_id == bytes([0x44, 0x12, 0xFF]):
                entity_name = 'Grinder'
            if entity_id == bytes([0x45, 0x00, 0xFF]) or entity_id == bytes([0x45, 0x12, 0xFF]):
                entity_name = 'Player'
            if entity_id == bytes([0x46, 0x00, 0xFF]) or entity_id == bytes([0x46, 0x12, 0xFF]):
                entity_name = '10-Coin'
            if entity_id == bytes([0x47, 0x00, 0xFF]) or entity_id == bytes([0x47, 0x12, 0xFF]):
                entity_name = 'Semisolid Platform (3D World)'
            if entity_id == bytes([0x48, 0x00, 0xFF]) or entity_id == bytes([0x48, 0x12, 0xFF]):
                entity_name = 'Koopa Troopa Car'
            if entity_id == bytes([0x49, 0x00, 0xFF]) or entity_id == bytes([0x49, 0x12, 0xFF]):
                entity_name = 'Toad'
            if entity_id == bytes([0x4A, 0x00, 0xFF]) or entity_id == bytes([0x4A, 0x12, 0xFF]):
                entity_name = 'None'
            if entity_id == bytes([0x4B, 0x00, 0xFF]) or entity_id == bytes([0x4B, 0x12, 0xFF]):
                entity_name = 'Stone'
            if entity_id == bytes([0x4C, 0x00, 0xFF]) or entity_id == bytes([0x4C, 0x12, 0xFF]):
                entity_name = 'Twister'
            if entity_id == bytes([0x4D, 0x00, 0xFF]) or entity_id == bytes([0x4D, 0x12, 0xFF]):
                entity_name = 'Boom Boom'
            if entity_id == bytes([0x4E, 0x00, 0xFF]) or entity_id == bytes([0x4E, 0x12, 0xFF]):
                entity_name = 'None'
            if entity_id == bytes([0x4F, 0x00, 0xFF]) or entity_id == bytes([0x4F, 0x12, 0xFF]):
                entity_name = 'None'
            if entity_id == bytes([0x50, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                entity_name = 'None'
            if entity_id == bytes([0x51, 0x00, 0xFF]) or entity_id == bytes([0x51, 0x12, 0xFF]):
                entity_name = 'Bumper'
            if entity_id == bytes([0x52, 0x00, 0xFF]) or entity_id == bytes([0x52, 0x12, 0xFF]):
                entity_name = 'Spike Pillar'
            if entity_id == bytes([0x53, 0x00, 0xFF]) or entity_id == bytes([0x53, 0x12, 0xFF]):
                entity_name = 'Snake Block'
            if entity_id == bytes([0x54, 0x00, 0xFF]) or entity_id == bytes([0x54, 0x12, 0xFF]):
                entity_name = 'Track Block'
            if entity_id == bytes([0x55, 0x00, 0xFF]) or entity_id == bytes([0x55, 0x12, 0xFF]):
                entity_name = 'Charvaargh'
            if entity_id == bytes([0x56, 0x00, 0xFF]) or entity_id == bytes([0x56, 0x12, 0xFF]):
                entity_name = 'Gentle Slope'
            if entity_id == bytes([0x57, 0x00, 0xFF]) or entity_id == bytes([0x57, 0x12, 0xFF]):
                entity_name = 'Steep Slope'
            if entity_id == bytes([0x58, 0x00, 0xFF]) or entity_id == bytes([0x58, 0x12, 0xFF]):
                entity_name = 'Custom Scroll Waypoint'
            if entity_id == bytes([0x59, 0x00, 0xFF]) or entity_id == bytes([0x59, 0x12, 0xFF]):
                entity_name = 'Checkpoint Flag'
            if entity_id == bytes([0x5A, 0x00, 0xFF]) or entity_id == bytes([0x5A, 0x12, 0xFF]):
                entity_name = 'Seesaw'
            if entity_id == bytes([0x5B, 0x00, 0xFF]) or entity_id == bytes([0x5B, 0x12, 0xFF]):
                entity_name = 'Pink Coin'
            if entity_id == bytes([0x5C, 0x00, 0xFF]) or entity_id == bytes([0x5C, 0x12, 0xFF]):
                entity_name = 'Clear Pipe'
            if entity_id == bytes([0x5D, 0x00, 0xFF]) or entity_id == bytes([0x5D, 0x12, 0xFF]):
                entity_name = 'Sloped Conveyer Belt'
            if entity_id == bytes([0x5E, 0x00, 0xFF]) or entity_id == bytes([0x5E, 0x12, 0xFF]):
                entity_name = 'Key'
            if entity_id == bytes([0x5F, 0x00, 0xFF]) or entity_id == bytes([0x5F, 0x12, 0xFF]):
                entity_name = 'Ant Trooper'
            if entity_id == bytes([0x60, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                entity_name = 'Warp Box'
            if entity_id == bytes([0x61, 0x00, 0xFF]) or entity_id == bytes([0x61, 0x12, 0xFF]):
                entity_name = 'Bowser Jr.'
            if entity_id == bytes([0x62, 0x00, 0xFF]) or entity_id == bytes([0x62, 0x12, 0xFF]):
                entity_name = 'On/Off Switch'
            if entity_id == bytes([0x63, 0x00, 0xFF]) or entity_id == bytes([0x63, 0x12, 0xFF]):
                entity_name = 'Dotted-Line Block'
            if entity_id == bytes([0x64, 0x00, 0xFF]) or entity_id == bytes([0x64, 0x12, 0xFF]):
                entity_name = 'Lava Editor'
            if entity_id == bytes([0x65, 0x00, 0xFF]) or entity_id == bytes([0x65, 0x12, 0xFF]):
                entity_name = 'Monty Mole'
            if entity_id == bytes([0x66, 0x00, 0xFF]) or entity_id == bytes([0x66, 0x12, 0xFF]):
                entity_name = 'Fish Bones'
            if entity_id == bytes([0x67, 0x00, 0xFF]) or entity_id == bytes([0x67, 0x12, 0xFF]):
                entity_name = 'Angry Sun'
            if entity_id == bytes([0x68, 0x00, 0xFF]) or entity_id == bytes([0x68, 0x12, 0xFF]):
                entity_name = 'Swinging Claw'
            if entity_id == bytes([0x69, 0x00, 0xFF]) or entity_id == bytes([0x69, 0x12, 0xFF]):
                entity_name = 'Tree'
            if entity_id == bytes([0x6A, 0x00, 0xFF]) or entity_id == bytes([0x6A, 0x12, 0xFF]):
                entity_name = 'Piranha Creeper'
            if entity_id == bytes([0x6B, 0x00, 0xFF]) or entity_id == bytes([0x6B, 0x12, 0xFF]):
                entity_name = 'Blinking Block'
            if entity_id == bytes([0x6C, 0x00, 0xFF]) or entity_id == bytes([0x6C, 0x12, 0xFF]):
                entity_name = 'Sound Effect Icon'
            if entity_id == bytes([0x6D, 0x00, 0xFF]) or entity_id == bytes([0x6D, 0x12, 0xFF]):
                entity_name = 'Spike Block'
            if entity_id == bytes([0x6E, 0x00, 0xFF]) or entity_id == bytes([0x6E, 0x12, 0xFF]):
                entity_name = 'None'
            if entity_id == bytes([0x6F, 0x00, 0xFF]) or entity_id == bytes([0x6F, 0x12, 0xFF]):
                entity_name = 'Crate'
            if entity_id == bytes([0x70, 0x00, 0xFF]) or entity_id == bytes([0x70, 0x12, 0xFF]):
                entity_name = 'Mushroom Trampoline'
            if entity_id == bytes([0x71, 0x00, 0xFF]) or entity_id == bytes([0x71, 0x12, 0xFF]):
                entity_name = 'Porcupuffer'
            if entity_id == bytes([0x72, 0x00, 0xFF]) or entity_id == bytes([0x72, 0x12, 0xFF]):
                entity_name = 'Goal Toadette'
            if entity_id == bytes([0x73, 0x00, 0xFF]) or entity_id == bytes([0x73, 0x12, 0xFF]):
                entity_name = 'Super Hammer'
            if entity_id == bytes([0x74, 0x00, 0xFF]) or entity_id == bytes([0x74, 0x12, 0xFF]):
                entity_name = 'Bully'
            if entity_id == bytes([0x75, 0x00, 0xFF]) or entity_id == bytes([0x75, 0x12, 0xFF]):
                entity_name = 'Icicle'
            if entity_id == bytes([0x76, 0x00, 0xFF]) or entity_id == bytes([0x76, 0x12, 0xFF]):
                entity_name = '! Block'
            print(str(i) + ': ' + str(entity_name) + ' @' + str(hex(608 + 32 * i)))


def print_entities():
    id = 0
    print('ID ' + hex(id) + ': Goomba/Galoomba')
    id += 1
    print('ID ' + hex(id) + ': Koopa Troopa')
    id += 1
    print('ID ' + hex(id) + ': Piranha Plant/Jumping Piranha Plant')
    id += 1
    print('ID ' + hex(id) + ': Hammer Bro')
    id += 1
    print('ID ' + hex(id) + ': Block')
    id += 1
    print('ID ' + hex(id) + ': ? Block')
    id += 1
    print('ID ' + hex(id) + ': Hard Block')
    id += 1
    print('ID ' + hex(id) + ': Ground')
    id += 1
    print('ID ' + hex(id) + ': Coin')
    id += 1
    print('ID ' + hex(id) + ': Pipe')
    id += 1
    print('ID ' + hex(id) + ': Trampoline')
    id += 1
    print('ID ' + hex(id) + ': Lift/Cloud Lift')
    id += 1
    print('ID ' + hex(id) + ': Thwomp')
    id += 1
    print('ID ' + hex(id) + ': Bill Blaster')
    id += 1
    print('ID ' + hex(id) + ': Mushroom Platform')
    id += 1
    print('ID ' + hex(id) + ': Bob-omb')
    id += 1
    print('ID ' + hex(id) + ': Semisolid Platform')
    id += 1
    print('ID ' + hex(id) + ': Bridge')
    id += 1
    print('ID ' + hex(id) + ': P-Switch')
    id += 1
    print('ID ' + hex(id) + ': Pow Block')
    id += 1
    print('ID ' + hex(id) + ': Super Mushroom')
    id += 1
    print('ID ' + hex(id) + ': Donut Block')
    id += 1
    print('ID ' + hex(id) + ': Cloud Block')
    id += 1
    print('ID ' + hex(id) + ': Note Block')
    id += 1
    print('ID ' + hex(id) + ': Fire Bar')
    id += 1
    print('ID ' + hex(id) + ': Spiny')
    id += 1
    print('ID ' + hex(id) + ': Ground Goal')
    id += 1
    print('ID ' + hex(id) + ': Goal Pole')
    id += 1
    print('ID ' + hex(id) + ': Buzzy Beetle')
    id += 1
    print('ID ' + hex(id) + ': Hidden Block')
    id += 1
    print('ID ' + hex(id) + ': Lakitu')
    id += 1
    print('ID ' + hex(id) + ': Cloud')
    id += 1
    print('ID ' + hex(id) + ': Banzai Bill')
    id += 1
    print('ID ' + hex(id) + ': 1-Up Mushroom')
    id += 1
    print('ID ' + hex(id) + ': Fire Flower')
    id += 1
    print('ID ' + hex(id) + ': Super Star')
    id += 1
    print('ID ' + hex(id) + ': Lava Lift')
    id += 1
    print('ID ' + hex(id) + ': Ground Start')
    id += 1
    print('ID ' + hex(id) + ': Start Sign')
    id += 1
    print('ID ' + hex(id) + ': Kameck')
    id += 1
    print('ID ' + hex(id) + ': Spike Top')
    id += 1
    print('ID ' + hex(id) + ': Boo')
    id += 1
    print('ID ' + hex(id) + ': Koopa CLown Car')
    id += 1
    print('ID ' + hex(id) + ': Spike Trap')
    id += 1
    print('ID ' + hex(id) + ': 3rd Tier Powerup')
    id += 1
    print('ID ' + hex(id) + ': Shoe Goomba/Yoshi Egg')
    id += 1
    print('ID ' + hex(id) + ': Dry Bones')
    id += 1
    print('ID ' + hex(id) + ': Cannon')
    id += 1
    print('ID ' + hex(id) + ': Blooper')
    id += 1
    print('ID ' + hex(id) + ': Castle Bridge')
    id += 1
    print('ID ' + hex(id) + ': Hop-Chops')
    id += 1
    print('ID ' + hex(id) + ': Skipsqueak')
    id += 1
    print('ID ' + hex(id) + ': Wiggler')
    id += 1
    print('ID ' + hex(id) + ': Conveyer Belt')
    id += 1
    print('ID ' + hex(id) + ': Burner')
    id += 1
    print('ID ' + hex(id) + ': Warp Door')
    id += 1
    print('ID ' + hex(id) + ': Cheep Cheep')
    id += 1
    print('ID ' + hex(id) + ': Muncher')
    id += 1
    print('ID ' + hex(id) + ': Rocky Wrench')
    id += 1
    print('ID ' + hex(id) + ': Rail')
    id += 1
    print('ID ' + hex(id) + ': Lava Bubble')
    id += 1
    print('ID ' + hex(id) + ': Chain Chomp')
    id += 1
    print('ID ' + hex(id) + ': Bowser/Meowser')
    id += 1
    print('ID ' + hex(id) + ': Ice Block')
    id += 1
    print('ID ' + hex(id) + ': Vine')
    id += 1
    print('ID ' + hex(id) + ': Stingby')
    id += 1
    print('ID ' + hex(id) + ': Arrow Sign')
    id += 1
    print('ID ' + hex(id) + ': One-Way Wall')
    id += 1
    print('ID ' + hex(id) + ': Grinder')
    id += 1
    print('ID ' + hex(id) + ': Player')
    id += 1
    print('ID ' + hex(id) + ': 10-Coin')
    id += 1
    print('ID ' + hex(id) + ': Semisolid Platform (3D World)')
    id += 1
    print('ID ' + hex(id) + ': Koopa Troopa Car')
    id += 1
    print('ID ' + hex(id) + ': Toad')
    id += 1
    print('ID ' + hex(id) + ': None')
    id += 1
    print('ID ' + hex(id) + ': Stone')
    id += 1
    print('ID ' + hex(id) + ': Twister')
    id += 1
    print('ID ' + hex(id) + ': Boom Boom')
    id += 1
    print('ID ' + hex(id) + ': None')
    id += 1
    print('ID ' + hex(id) + ': None')
    id += 1
    print('ID ' + hex(id) + ': None')
    id += 1
    print('ID ' + hex(id) + ': None')
    id += 1
    print('ID ' + hex(id) + ': Bumper')
    id += 1
    print('ID ' + hex(id) + ': Spike Pillar')
    id += 1
    print('ID ' + hex(id) + ': Snake Block')
    id += 1
    print('ID ' + hex(id) + ': Track Block')
    id += 1
    print('ID ' + hex(id) + ': Charvaargh')
    id += 1
    print('ID ' + hex(id) + ': Gentle Slope')
    id += 1
    print('ID ' + hex(id) + ': Steep Slope')
    id += 1
    print('ID ' + hex(id) + ': Custom Scroll Waypoint')
    id += 1
    print('ID ' + hex(id) + ': Checkpoint Flag')
    id += 1
    print('ID ' + hex(id) + ': Seesaw')
    id += 1
    print('ID ' + hex(id) + ': Pink Coin')
    id += 1
    print('ID ' + hex(id) + ': Clear Pipe')
    id += 1
    print('ID ' + hex(id) + ': Sloped Conveyer Belt')
    id += 1
    print('ID ' + hex(id) + ': Key')
    id += 1
    print('ID ' + hex(id) + ': Ant Trooper')
    id += 1
    print('ID ' + hex(id) + ': Warp Box')
    id += 1
    print('ID ' + hex(id) + ': Bowser Jr.')
    id += 1
    print('ID ' + hex(id) + ': On/Off Switch')
    id += 1
    print('ID ' + hex(id) + ': Dotted-Line Block')
    id += 1
    print('ID ' + hex(id) + ': Lava Editor')
    id += 1
    print('ID ' + hex(id) + ': Monty Mole')
    id += 1
    print('ID ' + hex(id) + ': Fish Bones')
    id += 1
    print('ID ' + hex(id) + ': Angry Sun')
    id += 1
    print('ID ' + hex(id) + ': Swinging Claw')
    id += 1
    print('ID ' + hex(id) + ': Tree')
    id += 1
    print('ID ' + hex(id) + ': Piranha Creeper')
    id += 1
    print('ID ' + hex(id) + ': Blinking Block')
    id += 1
    print('ID ' + hex(id) + ': Sound Effect Icon')
    id += 1
    print('ID ' + hex(id) + ': Spike Block')
    id += 1
    print('ID ' + hex(id) + ': None')
    id += 1
    print('ID ' + hex(id) + ': Crate')
    id += 1
    print('ID ' + hex(id) + ': Mushroom Trampoline')
    id += 1
    print('ID ' + hex(id) + ': Porcupuffer')
    id += 1
    print('ID ' + hex(id) + ': Goal Toadette')
    id += 1
    print('ID ' + hex(id) + ': Super Hammer')
    id += 1
    print('ID ' + hex(id) + ': Bully')
    id += 1
    print('ID ' + hex(id) + ': Icicle')
    id += 1
    print('ID ' + hex(id) + ': ! Block')


def read_all():
    global dec_course_path
    with open(dec_course_path,'rb') as course:
        for i in range(2600):
            course.seek(596 + 32 * i)
            entity_attribute = course.read(1)
            integer = int.from_bytes(entity_attribute, byteorder='big')
            hexadecimal = hex(integer)
            high, low = int(hexadecimal, 16) >> 4, int(hexadecimal, 16) & 0x0F
            high = hex(high)
            low = hex(low)
            if low == '0x0' or low == '0x8':
                status = 'Regular'
            if low == '0x1' or low == '0x9':
                status = 'In A Pipe'
            if low == '0x2' or low == '0xA':
                status = 'Winged'
            if low == '0x3' or low == '0xB':
                status = 'In Pipe And Winged'
            if low == '0x4' or low == '0xC':
                status = 'Shaken'
            if low == '0x5' or low == '0xD':
                status = 'Shaken In A Pipe'
            if low == '0x6' or low == '0xE':
                status = 'Shaken And Winged'
            if low == '0x7' or low == '0xF':
                status = 'Shaken And In Pipe And Winged'
            print(status + ' Entity ' + str(i) + ': ' + str(low) + ' @' + str(hex(628 + 32 * i)))


def edit_entity(entity_id_offset, new_id):
    global dec_course_path
    with open('C:/Users/User1/Desktop/test.bin', 'rb') as file:
	    data = file.read()
	    data = bytearray(data)
	    data[entity_id_offset] = int(new_id)
	    with open('C:/Users/User1/Desktop/test.bin', 'wb') as file:
		    file.write(data)
