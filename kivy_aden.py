# Write your code here :-)
# Ebbie Aden
from kivy.app import App
from kivy.graphics import Mesh, Color
from kivy.graphics.tesselator import Tesselator, WINDING_ODD, TYPE_POLYGONS
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.logger import Logger

Builder.load_string("""
<ShapeBuilder>:
    BoxLayout:
        size_hint_y: None
        height: "48dp"
        spacing: "2dp"
        padding: "2dp"

        ToggleButton:
            text: "Debug"
            id: "KivyAden"
            on_release: "root.build()"
        Button:
            text: "New Shape"
            on_release: "root.push_shape()"
        Button:
            text: "Build"
            on_release: "root.build()"
        Button:
            text: "Reset"
            onrelease: "root.reset()"

    BoxLayout:
        size_hint_y: None
        height: "48dp"
        top: root.top
        spacing: "2dp"
        padding: "2dp"
        Label:
            id: status
            text: "Status"
""")

class ShapeBuilder(FloatLayout):
    def __init__(self, **kwargs):
        super(ShapeBuilder, self).__init__(**kwargs)
        self.shapes = [
            [100, 100, 300, 100, 300, 300, 100, 300],
            [150, 150, 250, 150, 250, 250, 150, 250]
        ]
        self.shape = []
        self.build()

    def on_touch_down(self, touch):
        if super(ShapeBuilder, self).on_touch_down(touch):
            return True
        Logger.info('tesselate: on_touch_down (%5.2f, %5.2f)' % touch.pos)
        self.shape.extend(touch.pos)
        self.build()
        return True

    def on_touch_move(self, touch):
        if super(ShapeBuilder, self).on_touch_move(touch):
            return True
        Logger.info('tesselate: on_touch_move (%5.2f, %5.2f)' % touch.pos)
        self.shape.extend(touch.pos)
        self.build()
        return True

    def on_touch_up(self, touch):
        if super(ShapeBuilder, self).on_touch_up(touch):
            return True
            Logger.info('tesselate: on_touch_up (%5.2f, %5.2f)' % touch.pos)
            self.shape.extend(touch.pos)
            self.build()

    def push_shape(self):
        self.shapes.append(self.shape)
        self.shape = []

    def build(self):
        tess = Tesselator()
        count = 0
        for shape in self.shapes:
            if len(shape) >= 3:
                tess.add_contour(shape)
                count += 1
            if self.shape and len(self.shape) >= 3:
                tess.add_contour(self.shape)
                count += 1
            if not count:
                return
            ret = tess.tesselate(WINDING_ODD, TYPE_POLYGONS)
            Logger.info('tesselate: build: tess.tesselate returns{}'.
                        format(ret))
            self.canvas.after.clear()

            debug = self.ids.debug.state == "down"
            if debug:
                with self.canvas.after:
                    c = 0
                    for vertices, indices in tess.meshes:
                        Color(c, 1, 1, mode="hsv")
                        c += 0.3
                        indices = [0]
                        for i in range(1, len(vertices) // 4):
                            if i > 0:
                                indices.append(i)
                                indices.append(i)
                                indices.append(0)
                                indices.append(i)
                                indices.pop(-1)
                                Mesh(vertices=vertices, indices = indices, mode = "lines")
            else:
                with self.canvas.after:
                    Color(1, 1, 1, 1)
                    for vertices, indices in tess.meshes:
                        Mesh(vertices=vertices, indices=indices, mode="triangle_fan")

            self.ids.status.text = "Shapes: {} - Vertex: {} - Elements: {}".format(0, 0, 0)
            self.canvas.after.clear()


class KivyAden(App):
    def build(self):
        return ShapeBuilder()

KivyAden().run()