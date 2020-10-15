import pygame


class Button:
    def __init__(self, image, center, button_press_command, screen_size, scale_factor, call, scene=None, list_to_append=None):
        self.screen_size = screen_size
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (round(screen_size[0] / scale_factor[0]), round(screen_size[1] / scale_factor[1])))
        self.center = center
        if scene is not None:
            self.scene = scene
            scene.append(self)
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.center[0] - (self.rect[2] // 2), self.center[1] - (self.rect[3] // 2), self.rect[2], self.rect[3])

        # Making a hover over version of itself (lighter and slightly bigger)
        self.image_lighter = self.image.copy()
        self.image_lighter = brighten_image(self.image_lighter, 20)
        self.image_lighter = pygame.transform.scale(self.image_lighter, (int(self.rect[2] * 1.2), int(self.rect[3] * 1.2)))

        # Making a press down version of itself (darker)
        self.image_darker = self.image.copy()
        self.image_darker = darken_image(self.image_darker, 50)

        # Start by displaying default version of itself
        self.image_to_display = self.image
        self.is_hovering = False
        self.is_pressed_down = False
        self.is_pressed_up = False
        self.button_press_command = button_press_command
        self.call_events = call
        self.is_active = False
        if list_to_append is not None:
            list_to_append.append(self)

    def __repr__(self):
        return "Button: " + str(self.button_press_command)

    def state_check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.is_hovering:
            self.is_hovering = False

        if self.rect[0] + self.rect[2] > mouse_pos[0] > self.rect[0] and self.rect[1] + self.rect[3] > mouse_pos[
            1] > self.rect[1] and not self.is_hovering and self.is_active:
            self.is_hovering = True

        if self.is_pressed_up:
            self.button_press_command()
            self.is_pressed_up = False

        if self.is_hovering and not self.is_pressed_down:
            self.image_to_display = self.image_lighter
        elif self.is_pressed_down and self.is_hovering:
            self.image_to_display = self.image_darker
        else:
            self.image_to_display = self.image

        for event in self.call_events:
            if not event:
                self.is_active = False
        for event in self.call_events:
            if event:
                self.is_active = True

    def get_center_cor(self):
        if self.is_hovering and not self.is_pressed_down:
            return self.center[0] - ((self.rect[2] * 1.2) // 2), self.center[1] - ((self.rect[3] * 1.2) // 2)
        elif not self.is_hovering or self.is_pressed_down:
            return self.center[0] - (self.rect[2] // 2), self.center[1] - (self.rect[3] // 2)

# Function that brightens image by certain amount
def brighten_image(image, brighten):
    image.fill((brighten, brighten, brighten), special_flags=pygame.BLEND_RGB_ADD)
    return image


# Function that darkens image by certain amount
def darken_image(image, darken):
    image.fill((darken, darken, darken), special_flags=pygame.BLEND_RGB_SUB)
    return image