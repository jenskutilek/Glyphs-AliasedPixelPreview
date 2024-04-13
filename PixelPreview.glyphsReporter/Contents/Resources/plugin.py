from __future__ import annotations
import objc
from AppKit import NSBezierPath, NSColor, NSPoint
from GlyphsApp import Glyphs
from GlyphsApp.plugins import ReporterPlugin


class PixelPreview(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = Glyphs.localize(
            {
                "en": "PixelPreview",
                "de": "Pixelvorschau",
            }
        )

    @objc.python_method
    def foreground(self, layer):
        NSColor.controlTextColor().set()
        NSBezierPath.fillRect_(layer.bounds)
        self.drawTextAtPoint(layer.parent.name, NSPoint(0, 0))

    @objc.python_method
    def inactiveLayerForeground(self, layer):
        NSColor.selectedTextColor().set()
        if layer.paths:
            layer.bezierPath.fill()
        if layer.components:
            NSColor.findHighlightColor().set()
            for component in layer.components:
                component.bezierPath.fill()

    @objc.python_method
    def preview(self, layer):
        NSColor.textColor().set()
        if layer.paths:
            layer.bezierPath.fill()
        if layer.components:
            NSColor.highlightColor().set()
            for component in layer.components:
                component.bezierPath.fill()

    def doSomething_(self, sender):
        print("Just did something")

    def doSomethingElse_(self, sender):
        print("Just did something else")

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
