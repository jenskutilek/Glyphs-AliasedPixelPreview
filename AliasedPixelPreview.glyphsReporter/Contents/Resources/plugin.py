from __future__ import annotations

import objc
from AppKit import NSBezierPath, NSClassFromString, NSColor, NSRect
from GlyphsApp import Glyphs
from GlyphsApp.plugins import ReporterPlugin


PIXEL_COLOR = (0, 0, 0, 0.15)


class AliasedPixelPreview(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = Glyphs.localize(
            {
                "en": "Aliased Pixel Preview",
                "de": "Schwarzweiß-Pixelvorschau",
            }
        )

    @objc.python_method
    def background(self, layer):
        currentController = self.controller.view().window().windowController()
        if currentController:
            tool = currentController.toolDrawDelegate()
            # don't activate if on cursor tool, or pan tool
            if (
                tool.isKindOfClass_(NSClassFromString("GlyphsToolText"))
                or tool.isKindOfClass_(NSClassFromString("GlyphsToolHand"))
                or tool.isKindOfClass_(
                    NSClassFromString("GlyphsToolTrueTypeInstructor")
                )
            ):
                return

        NSColor.colorWithCalibratedRed_green_blue_alpha_(*PIXEL_COLOR).set()
        outline = layer.completeBezierPath
        font = layer.font()
        step = font.upm // int(Glyphs.defaults.get("PixelPreviewPixel", 18))
        halfstep = step // 2
        for y in range(-400 // step, 1200 // step + step):
            for x in range(0, int(layer.width // step) + step):
                if outline.containsPoint_((x * step + halfstep, y * step + halfstep)):
                    NSBezierPath.fillRect_(
                        NSRect(origin=(x * step, y * step), size=(step, step))
                    )

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
