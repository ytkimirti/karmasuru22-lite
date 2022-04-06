from . import cmd_interop
import struct


def crash_enabled(enabled):
    cmd_interop.send_message([1, 2 if enabled else 1])


def limits_enabled(enabled):
    cmd_interop.send_message([1, 4 if enabled else 3])


def show_nodes(enabled):
    cmd_interop.send_message([1, 5 if enabled else 6])


def show_limits(enabled):
    cmd_interop.send_message([1, 7 if enabled else 8])


def infinite_supply(enabled):
    cmd_interop.send_message([1, 15 if enabled else 16])


def spawn_3d_text(text_id, pos_x, pos_y, pos_z, color_r, color_g, color_b, text):
    data = [1, 9]
    for i in text_id.to_bytes(4, "big"):
        data.append(i)
    for i in struct.pack('>f', pos_x):
        data.append(i)
    for i in struct.pack('>f', pos_y):
        data.append(i)
    for i in struct.pack('>f', pos_z):
        data.append(i)
    for i in color_r.to_bytes(1, "big"):
        data.append(i)
    for i in color_g.to_bytes(1, "big"):
        data.append(i)
    for i in color_b.to_bytes(1, "big"):
        data.append(i)
    for i in str.encode(text, encoding="utf-8"):
        data.append(i)
    cmd_interop.send_message(data)


def destroy_3d_text(text_id):
    data = [1, 10]
    for i in text_id.to_bytes(4, "big"):
        data.append(i)
    cmd_interop.send_message(data)


def move_3d_text(text_id, pos_x, pos_y, pos_z):
    data = [1, 11]
    for i in text_id.to_bytes(4, "big"):
        data.append(i)
    for i in struct.pack('>f', pos_x):
        data.append(i)
    for i in struct.pack('>f', pos_y):
        data.append(i)
    for i in struct.pack('>f', pos_z):
        data.append(i)
    cmd_interop.send_message(data)


def spawn_sphere(sphere_id, pos_x, pos_y, pos_z, color_r, color_g, color_b, radius):
    data = [1, 12]
    for i in sphere_id.to_bytes(4, "big"):
        data.append(i)
    for i in struct.pack('>f', pos_x):
        data.append(i)
    for i in struct.pack('>f', pos_y):
        data.append(i)
    for i in struct.pack('>f', pos_z):
        data.append(i)
    for i in color_r.to_bytes(1, "big"):
        data.append(i)
    for i in color_g.to_bytes(1, "big"):
        data.append(i)
    for i in color_b.to_bytes(1, "big"):
        data.append(i)
    for i in struct.pack('>f', radius):
        data.append(i)
    cmd_interop.send_message(data)


def destroy_sphere(sphere_id):
    data = [1, 13]
    for i in sphere_id.to_bytes(4, "big"):
        data.append(i)
    cmd_interop.send_message(data)


def move_sphere(sphere_id, pos_x, pos_y, pos_z):
    data = [1, 14]
    for i in sphere_id.to_bytes(4, "big"):
        data.append(i)
    for i in struct.pack('>f', pos_x):
        data.append(i)
    for i in struct.pack('>f', pos_y):
        data.append(i)
    for i in struct.pack('>f', pos_z):
        data.append(i)
    cmd_interop.send_message(data)
