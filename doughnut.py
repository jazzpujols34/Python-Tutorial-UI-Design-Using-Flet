"""  Flet UI Desing Front-End """

# modules / imports
import flet
from flet import (
    Image,
    Page,
    UserControl,
    Column,
    Row,
    Text,
    Container,
    padding,
    alignment,
    border,
    transform,
    border_radius,
    animation,
)


class Doughnut(UserControl):
    def animate_content(self, e):
        if e.control.scale != 1.25:
            e.control.scale = 1.25
        else:
            e.control.scale = 1
        e.control.update()

    def Ingredient(self, macro, amount, color, percent):
        return Container(
            scale=transform.Scale(0.9),
            alignment=alignment.center,
            width=60,
            height=100,
            border=border.all(1, 'black'),
            padding=5,
            border_radius=border_radius.all(30),
            content=Column(
                horizontal_alignment='center',
                alignment='center',
                spacing=5,
                controls=[
                    Text(value=macro, size=10, weight='bold', color='black'),
                    Text(value=amount, size=8, italic=True, color='black'),
                    Container(
                        width=35,
                        height=35,
                        bgcolor=color,
                        border_radius=35,
                        alignment=alignment.center,
                        scale=transform.Scale(1),
                        animate_scale=animation.Animation(
                            duration=900, curve='bounceOut'
                        ),
                        on_hover=lambda e: self.animate_content(
                            e),  # Moved this line here
                        content=Text(
                            value=percent,
                            color='black',
                            size=11,
                            weight='w600',
                            text_align='center',
                        ),
                    ),
                ],
            ),
        )

        pass

    def MainContainer(self):
        # MAIN CONTAINER
        self._main = Container(
            width=280,
            height=600,
            bgcolor="#ffb6c1",
            border_radius=30,
            padding=10,
        )

        # IMAGE
        self.img = Image(
            src='./assets/doughnut.png',
            width=230,
            height=230,
            offset=transform.Offset(0, -0.1),
            animate_offset=animation.Animation(),
        )

        self.sugar = self.Ingredient('Sugar', '25 grams', 'blue600', '13%')
        self.salt = self.Ingredient('Salt', '250 grams', 'pink300', '11%')
        self.fat = self.Ingredient('Fat', '6 grams', 'pink400', '8%')
        self.energy = self.Ingredient('Energy', '220 Kcal', 'pink300', '11%')

        # MAIN COLUMN
        self._main_col = Column(
            controls=[
                Container(
                    width=self._main.width,
                    height=self._main.height * 0.45,
                    bgcolor="#fffeff",
                    border_radius=30,
                    content=Column(
                        spacing=0,
                        controls=[
                            Row(
                                controls=[
                                    Container(
                                        padding=20,
                                        content=Text(
                                            "← Bostolicious Cream",
                                            size=14,
                                            weight='w600',
                                            color="black",
                                        ),
                                    )
                                ]
                            ),
                            # IMAGE ROW
                            Row(
                                alignment="center",
                                controls=[
                                    self.img,
                                ],

                            ),

                        ],
                    ),
                ),
                Container(
                    padding=10,
                    width=self._main.width,
                    height=self._main.height * 0.54,
                    bgcolor="#fffeff",
                    border_radius=border_radius.all(20),
                    offset=transform.Offset(0, -0.07),
                    animate_offset=animation.Animation(),
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Container(padding=10),
                            Row(
                                controls=[
                                    Text(
                                        'Nutrition Value',
                                        color='black',
                                        weight='bold',
                                    )
                                ]
                            ),
                            Container(
                                content=Row(
                                    alignment='center',
                                    vertical_alignment='center',
                                    spacing=0,
                                    controls=[
                                        # VALUES HERE
                                        self.sugar,
                                        self.salt,
                                        self.fat,
                                        self.energy,
                                    ],
                                )
                            ),
                            Row(
                                controls=[
                                    Text(
                                        "Description",
                                        color='black',
                                        weight='bold',
                                    )
                                ]
                            ),
                            Row(
                                wrap=True,
                                controls=[
                                    Text("The Sweet and Subtle Salty Combo of Chocolate meets Caramel, Introduce The Caramel Duo to Your Mouth!",
                                         color='black',
                                         weight='w300',
                                         size=9,
                                         )
                                ],
                            ),
                            Row(
                                alignment='center',
                                controls=[
                                    Container(
                                        width=self._main.width * 0.8,
                                        height=45,
                                        border_radius=8,
                                        border=border.all(1, "black"),
                                        content=Row(
                                            alignment="spaceAround",
                                            controls=[
                                                Column(
                                                    alignment='center',
                                                    spacing=1,
                                                    controls=[
                                                        Text("$12.75",
                                                             color='black',
                                                             weight='bold',
                                                             size=12,
                                                             ),
                                                        Text("Description Not Included",
                                                             color='black',
                                                             weight='w500',
                                                             size=8,
                                                             ),
                                                    ],
                                                ),
                                                Container(
                                                    content=Text(
                                                        "ADD!",
                                                        color="black",
                                                        weight="w700",
                                                    )
                                                )
                                            ],
                                        ),
                                    )
                                ],
                            ),
                        ]
                    ),
                ),
            ]
        )

        #
        self._main.content = self._main_col

        return self._main

    def build(self):
        return Column(
            expand=True,
            alignment="center",
            controls=[
                self.MainContainer(),
            ],
        )


def start(page: Page):
    page.title = 'Doughnut App'
    app = Doughnut()
    page.add(app)
    page.update()


if __name__ == '__main__':
    flet.app(target=start, assets_dir='assets')
