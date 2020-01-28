import sys, os, os.path, tkinter
from tkinter import filedialog, messagebox


def encrypt_course():
    global dec_course_path
    with open('path/decryptor_path.txt','r') as decryptor_path:
            dec_path = decryptor_path.read()
            os.system(dec_path + ' -e ' + dec_course_path + ' ' + str(dec_course_path).replace('dec_',''))


def open_enc_course():
    global dec_course_path
    home = os.path.expanduser("~")
    root = tkinter.Tk()
    root.withdraw()
    course_path = filedialog.askopenfilename(initialdir = home + "/Desktop",title = "Select An Encrypted Super Mario Maker 2 Course Data File",filetypes = (("Binary Course Data Files","*.bcd"),("All Files","*.*")))
    if course_path:
        head, tail = os.path.split(course_path)
        dec_course_path = head + '\dec_' + tail
        with open('path/decryptor_path.txt','r') as decryptor_path:
            dec_path = decryptor_path.read()
            os.system(dec_path + ' -h ' + course_path + ' ' + dec_course_path)
            print(course_path)
    else:
        print('You Chose Nothing!')


def import_enc_course_path():
    global dec_course_path
    with open('path/enc_course_path.txt','r') as course_path:
        enc_course_path = course_path.read()
        head, tail = os.path.split(enc_course_path)
        dec_course_path = head + '\dec_' + tail
        with open('path/decryptor_path.txt','r') as decryptor_path:
            dec_path = decryptor_path.read()
            os.system(dec_path + ' -h ' + enc_course_path + ' ' + dec_course_path)
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
    with open('path/dec_course_path.txt','r') as course_path:
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


def read_coordinates():
    global dec_course_path
    with open(dec_course_path,'rb') as course:
        for i in range(2600):
            course.seek(584 + 32 * i)
            entity_coordinates = course.read(8)
            print('Entity ' + str(i) + ' Coordinates: ' + str(entity_coordinates) + ' @' + str(hex(628 + 32 * i)))


def read_dimensions():
    global dec_course_path
    with open(dec_course_path,'rb') as course:
        for i in range(2600):
            course.seek(562 + 32 * i)
            entity_dimensions = course.read(2)
            print('Entity ' + str(i) + ' Dimensions: ' + str(entity_dimensions) + ' @' + str(hex(628 + 32 * i)))


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
            home = os.path.expanduser("~")
            os.system('echo ' + (str(i) + ': ' + str(entity_name) + ' @' + str(hex(608 + 32 * i))) + ' >> ' + home + '/Desktop/extracted_entities.txt')
    print('Entities exported to ' + home + '/Desktop/extracted_entities.txt')


def print_entities():
    id = 0
    print('ID ' + str(id) + ', ' + hex(id) + ': Goomba/Galoomba')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Koopa Troopa')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Piranha Plant/Jumping Piranha Plant')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Hammer Bro')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': ? Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Hard Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Ground')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Coin')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Pipe')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Trampoline')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Lift/Cloud Lift')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Thwomp')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Bill Blaster')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Mushroom Platform')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Bob-omb')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Semisolid Platform')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Bridge')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': P-Switch')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Pow Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Super Mushroom')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Donut Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Cloud Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Note Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Fire Bar')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Spiny')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Ground Goal')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Goal Pole')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Buzzy Beetle')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Hidden Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Lakitu')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Cloud')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Banzai Bill')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': 1-Up Mushroom')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Fire Flower')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Super Star')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Lava Lift')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Ground Start')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Start Sign')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Kameck')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Spike Top')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Boo')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Koopa CLown Car')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Spike Trap')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': 3rd Tier Powerup')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Shoe Goomba/Yoshi Egg')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Dry Bones')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Cannon')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Blooper')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Castle Bridge')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Hop-Chops')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Skipsqueak')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Wiggler')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Conveyer Belt')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Burner')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Warp Door')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Cheep Cheep')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Muncher')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Rocky Wrench')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Rail')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Lava Bubble')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Chain Chomp')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Bowser/Meowser')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Ice Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Vine')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Stingby')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Arrow Sign')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': One-Way Wall')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Grinder')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Player')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': 10-Coin')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Semisolid Platform (3D World)')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Koopa Troopa Car')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Toad')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': None')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Stone')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Twister')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Boom Boom')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': None')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': None')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': None')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': None')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Bumper')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Spike Pillar')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Snake Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Track Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Charvaargh')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Gentle Slope')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Steep Slope')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Custom Scroll Waypoint')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Checkpoint Flag')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Seesaw')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Pink Coin')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Clear Pipe')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Sloped Conveyer Belt')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Key')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Ant Trooper')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Warp Box')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Bowser Jr.')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': On/Off Switch')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Dotted-Line Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Lava Editor')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Monty Mole')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Fish Bones')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Angry Sun')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Swinging Claw')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Tree')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Piranha Creeper')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Blinking Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Sound Effect Icon')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Spike Block')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': None')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Crate')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Mushroom Trampoline')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Porcupuffer')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Goal Toadette')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Super Hammer')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Bully')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': Icicle')
    id += 1
    print('ID ' + str(id) + ', ' + hex(id) + ': ! Block')


def edit_entity(entity_name, entity_number):
    global dec_course_path
    if entity_name == 'Goomba' or entity_name == 'Galoomba':
        new_id = 0x00
    if entity_name == 'Koopa Troopa':
        new_id = 0x01
    if entity_name == 'Piranha Plant' or entity_name == 'Jumping Piranha Plant':
        new_id = 0x02
    if entity_name == 'Hammer Bro':
        new_id = 0x03
    if entity_name == 'Block':
        new_id = 0x04
    if entity_name == '? Block':
        new_id = 0x05
    if entity_name == 'Hard Block':
        new_id = 0x06
    if entity_name == 'Ground':
        new_id = 0x07
    if entity_name == 'Coin':
        new_id = 0x08
    if entity_name == 'Pipe':
        new_id = 0x09
    if entity_name == 'Trampoline':
        new_id = 0x0A
    if entity_name == 'Lift' or entity_name == 'Cloud Lift':
        new_id = 0x0B
    if entity_name == 'Thwomp':
        new_id = 0x0C
    if entity_name == 'Bill Blaster':
        new_id = 0x0D
    if entity_name == 'Mushroom Platform':
        new_id = 0x0E
    if entity_name == 'Bob-Omb':
        new_id = 0x0F
    if entity_name == 'Semisolid Platform':
        new_id = 0x10
    if entity_name == 'Bridge':
        new_id = 0x11
    if entity_name == 'P-Switch':
        new_id = 0x12
    if entity_name == 'Pow Block':
        new_id = 0x13
    if entity_name == 'Super Mushroom':
        new_id = 0x14
    if entity_name == 'Donut Block':
        new_id = 0x15
    if entity_name == 'Cloud Block':
        new_id = 0x16
    if entity_name == 'Note Block':
        new_id = 0x17
    if entity_name == 'Firebar':
        new_id = 0x18
    if entity_name == 'Spiny':
        new_id = 0x19
    if entity_name == 'Ground Goal':
        new_id = 0x1A
    if entity_name == 'Goal Pole':
        new_id = 0x1B
    if entity_name == 'Buzzy Beatle':
        new_id = 0x1C
    if entity_name == 'Hidden Block':
        new_id = 0x1D
    if entity_name == 'Lakitu':
        new_id = 0x1E
    if entity_name == 'Cloud':
        new_id = 0x1F
    if entity_name == 'Banzai Bill':
        new_id = 0x20
    if entity_name == '1-Up Mushroom':
        new_id = 0x21
    if entity_name == 'Fire Flower':
        new_id = 0x22
    if entity_name == 'Super Star':
        new_id = 0x23
    if entity_name == 'Lava lift':
        new_id = 0x24
    if entity_name == 'Ground Start':
        new_id = 0x25
    if entity_name == 'Start Arrow':
        new_id = 0x26
    if entity_name == 'Kameck':
        new_id = 0x27
    if entity_name == 'Spike Top':
        new_id = 0x28
    if entity_name == 'Boo':
        new_id = 0x29
    if entity_name == 'Koopa Clown Car':
        new_id = 0x2A
    if entity_name == 'Spike Trap':
        new_id = 0x2B
    if entity_name == '3rd Tier Powerup':
        new_id = 0x2C
    if entity_name == 'Shoe Goomba' or entity_name == 'Yoshi Egg':
        new_id = 0x2D
    if entity_name == 'Dry Bones':
        new_id = 0x2E
    if entity_name == 'Cannon':
        new_id = 0x2F
    if entity_name == 'Blooper':
        new_id = 0x30
    if entity_name == 'Castle Bridge':
        new_id = 0x31
    if entity_name == 'Hop-Chops':
        new_id = 0x32
    if entity_name == 'Skipsqueak':
        new_id = 0x33
    if entity_name == 'Wiggler':
        new_id = 0x34
    if entity_name == 'Conveyer Belt':
        new_id = 0x35
    if entity_name == 'Burner':
        new_id = 0x36
    if entity_name == 'Warp Door':
        new_id = 0x37
    if entity_name == 'Cheep Cheep':
        new_id = 0x38
    if entity_name == 'Muncher':
        new_id = 0x39
    if entity_name == 'Rocky Wrench':
        new_id = 0x3A
    if entity_name == 'Rail':
        new_id = 0x3B
    if entity_name == 'Lava Bubble':
        new_id = 0x3C
    if entity_name == 'Chain Chomp':
        new_id = 0x3D
    if entity_name == 'Bowser' or entity_name == 'Meowser':
        new_id = 0x3E
    if entity_name == 'Ice Block':
        new_id = 0x3F
    if entity_name == 'Vine':
        new_id = 0x40
    if entity_name == 'Stingby':
        new_id = 0x41
    if entity_name == 'Arrow Sign':
        new_id = 0x42
    if entity_name == 'One-Way Wall':
        new_id = 0x43
    if entity_name == 'Grinder':
        new_id = 0x44
    if entity_name == 'Player':
        new_id = 0x45
    if entity_name == '10-Coin':
        new_id = 0x46
    if entity_name == 'Semisolid Platform (3D World)':
        new_id = 0x47
    if entity_name == 'Koopa Troopa Car':
        new_id = 0x48
    if entity_name == 'Toad':
        new_id = 0x49
    if entity_name == 'None':
        new_id = 0x4A
    if entity_name == 'Stone':
        new_id = 0x4B
    if entity_name == 'Twister':
        new_id = 0x4C
    if entity_name == 'Boom Boom':
        new_id = 0x4D
    if entity_name == 'None':
        new_id = 0x4E
    if entity_name == 'None':
        new_id = 0x4F
    if entity_name == 'None':
        new_id = 0x50
    if entity_name == 'None':
        new_id = 0x51
    if entity_name == 'Bumper':
        new_id = 0x52
    if entity_name == 'Spike Pillar':
        new_id = 0x53
    if entity_name == 'Snake Block':
        new_id = 0x54
    if entity_name == 'Track Block':
        new_id = 0x55
    if entity_name == 'Charvaargh':
        new_id = 0x56
    if entity_name == 'Gentle Slope':
        new_id = 0x57
    if entity_name == 'Steep Slope':
        new_id = 0x58
    if entity_name == 'Custom Scroll Waypoint':
        new_id = 0x59
    if entity_name == 'Checkpoint Flag':
        new_id = 0x5A
    if entity_name == 'Seesaw':
        new_id = 0x5B
    if entity_name == 'Pink Coin':
        new_id = 0x5C
    if entity_name == 'Clear Pipe':
        new_id = 0x5D
    if entity_name == 'Sloped Conveyer Belt':
        new_id = 0x5E
    if entity_name == 'Key':
        new_id = 0x5F
    if entity_name == 'Ant Trooper':
        new_id = 0x60
    if entity_name == 'Warp Box':
        new_id = 0x61
    if entity_name == 'Bowser Jr.':
        new_id = 0x62
    if entity_name == 'On/Off Switch':
        new_id = 0x63
    if entity_name == 'Dotted-Line Block':
        new_id = 0x64
    if entity_name == 'Lava Editor':
        new_id = 0x65
    if entity_name == 'Monty Mole':
        new_id = 0x66
    if entity_name == 'Fish Bones':
        new_id = 0x67
    if entity_name == 'Angry Sun':
        new_id = 0x68
    if entity_name == 'Swinging Claw':
        new_id = 0x69
    if entity_name == 'Tree':
        new_id = 0x6A
    if entity_name == 'Piranha Creeper':
        new_id = 0x6B
    if entity_name == 'Blinking Block':
        new_id = 0x6C
    if entity_name == 'Sound Effect Icon':
        new_id = 0x6D
    if entity_name == 'Spike Block':
        new_id = 0x6E
    if entity_name == 'None':
        new_id = 0x6F
    if entity_name == 'Crate':
        new_id = 0x70
    if entity_name == 'Mushroom Trampoline':
        new_id = 0x71
    if entity_name == 'Porcupuffer':
        new_id = 0x72
    if entity_name == 'Goal Toadette':
        new_id = 0x73
    if entity_name == 'Super Hammer':
        new_id = 0x74
    if entity_name == 'Bully':
        new_id = 0x75
    if entity_name == 'Icicle':
        new_id = 0x76
    if entity_name == '! Block':
        new_id = 0x77
    with open(dec_course_path, 'rb') as course:
	    data = course.read()
	    data = bytearray(data)
	    data[576 + 32 * entity_number] = int(new_id)
	    with open(dec_course_path, 'wb') as course:
		    course.write(data)
		    print('Success!')


def edit_key_status(entity_number, key_status):
    global dec_course_path
    if key_status == False:
        key = 0x00
    if key_status == True:
        key = 0x12
    with open(dec_course_path, 'rb') as course:
        data = course.read()
        data = bytearray(data)
        data[577 + 32 * entity_number] = int(key)
        with open(dec_course_path, 'wb') as course:
            course.write(data)
            print('Success!')

def remove_entity(entity_number):
    global dec_course_path
    if entity_number < 1:
        print('Enemy Number Cannot Be Less Than 1!')
        return
    if entity_number > 2599:
        print('Enemy Number Cannot Be More Than 2599!')
        return
    with open(dec_course_path, 'rb') as course:
        data = course.read()
        data = bytearray(data)
        data[int(552 + 32 * entity_number):int(552 + 32 * entity_number + 32)] = bytes([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
        with open(dec_course_path, 'wb') as course:
            course.write(data)

def add_new_basic_entity():
    global i
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
            if entity_name == f'Unknown({entity_id})':
                with open(dec_course_path,'rb') as course:
                    data = course.read()
                    data = bytearray(data)
                    data[608 + 32 * i - 24:608 + 32 * i + 32 - 24] = b'\xB0\x04\x00\x00\xF0\x00\x00\x00\x00\x00\x01\x01\x40\x00\x00\x06\x40\x00\x00\x06\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF'
                    with open(dec_course_path,'wb') as course:
                        course.write(data)
                        print('Success!')
                        return
