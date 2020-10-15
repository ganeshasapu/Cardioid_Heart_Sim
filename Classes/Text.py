import pygame

count = 0


class Text:

    def __init__(self, text, colour, font, center, screen_size, scale_factor, scene=None, list_to_append=None):
        font_used = pygame.font.Font(font, round(screen_size[0] / scale_factor))
        rendered_text = font_used.render(text, True, colour, None)
        self.text = text
        self.size = (rendered_text.get_width(), rendered_text.get_height())
        if scene is not None:
            self.scene = scene
            scene.append(self)

        self.image_to_display = rendered_text
        self.initialized = False
        self.center = center
        if list_to_append is not None:
            list_to_append.append(self)

    def get_center_cor(self):
        return self.center[0] - (self.size[0] // 2), self.center[1] - (self.size[1] // 2)

    def __repr__(self):
        return "Text: " + self.text