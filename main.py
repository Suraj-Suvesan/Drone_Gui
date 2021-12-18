import dearpygui.dearpygui as dpg
from easytello import tello

drone = tello.Tello()


def stats():
    c = drone.get_battery()
    d = drone.get_height()
    e = drone.get_acceleration()
    f = drone.get_attitude()
    g = drone.get_temp()
    dpg.set_value(
        "stats",
        f"stats \nbattery: {c}, \nheight:{d}, \nacceleration{e}, \nattitude{f}, \ntemprature{g}",
    )


dpg.create_context()

with dpg.window(label="Basic Movement", pos=(100, 0), autosize=True):
    dpg.add_button(label="forward", callback=lambda: drone.forward(20))
    dpg.add_button(label="backward", callback=lambda: drone.back(20))
    dpg.add_button(label="left", callback=lambda: drone.left(20))
    dpg.add_button(label="right", callback=lambda: drone.right(20))

with dpg.window(label="Complex Movement", pos=(300, 0), autosize=True):
    dpg.add_button(label="Rotate 90 Degrees (cw)", callback=lambda: drone.cw(90))
    dpg.add_button(label="Rotate 90 Degrees (ccw)", callback=lambda: drone.cw(-90))
    dpg.add_button(label="Flip", callback=lambda: drone.flip("f"))
    dpg.add_button(label="Decrease Altitude", callback=lambda: drone.down(20))
    dpg.add_button(label="Increase Altitude", callback=lambda: drone.up(20))

with dpg.window(label="Misc", pos=(500, 0), autosize=True):
    dpg.add_button(label="Takeoff", callback=lambda: drone.takeoff())
    dpg.add_button(label="Land", callback=lambda: drone.land())
    dpg.add_button(label="Check Stats", callback=stats)
    dpg.add_text("stats", tag="stats")

dpg.create_viewport(title="Custom Title", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
