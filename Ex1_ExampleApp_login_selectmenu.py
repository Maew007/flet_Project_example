import flet as ft


# ฟังก์ชันที่สร้างหน้า Home Page หลังจากเข้าสู่ระบบสำเร็จ
def home_page(page):
    # ตั้งค่าหน้า Home
    page.title = "Home Page"
    page.clean()  # ลบองค์ประกอบเก่าทั้งหมด
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ฟังก์ชันเมื่อมีการคลิกเปลี่ยนหน้าใน NavigationBar
    def on_nav_change(e):
        if e.control.selected_index == 0:
            home_page(page)  # กลับไปที่หน้า Home
        elif e.control.selected_index == 1:
            menu1_page(page)  # ไปที่หน้า Page1
        elif e.control.selected_index == 2:
            menu2_page(page)  # ไปที่หน้า Page2
        elif e.control.selected_index == 3:
            menu3_page(page)  # ไปที่หน้า Page3

    # องค์ประกอบในหน้า Home
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Page Home", size=30, weight=ft.FontWeight.BOLD),
                        ft.CircleAvatar(
                            foreground_image_url="https://via.placeholder.com/100",
                            radius=30,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row([
                            ft.Image(src="https://picsum.photos/150/150?6", width=200, height=200),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,    
                        ),         
                
                ft.NavigationBar(
                    destinations=[
                        ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                        ft.NavigationDestination(icon=ft.icons.CAR_RENTAL, label="Page1"),
                        ft.NavigationDestination(icon=ft.icons.GROUP, label="Page2"),
                        ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile"),
                    ],
                    selected_index=0,
                    on_change=on_nav_change  # เพิ่ม callback เพื่อเปลี่ยนหน้า
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )


# #ฟังก์ชันที่สร้างหน้าเมนู 1
def menu1_page(page):
    # ตั้งค่าหน้าเมนู 1
    page.title = "หน้ารายละเอียด 1"
    page.clean()  # ลบองค์ประกอบเก่าทั้งหมด
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ฟังก์ชันเมื่อมีการคลิกเปลี่ยนหน้าใน NavigationBar
    def on_nav_change(e):
        if e.control.selected_index == 0:
            home_page(page)  # กลับไปที่หน้า Home
        elif e.control.selected_index == 1:
            menu1_page(page)  # ไปที่หน้า Page1
        elif e.control.selected_index == 2:
            menu2_page(page)  # ไปที่หน้า Page2
        elif e.control.selected_index == 3:
            menu3_page(page)  # ไปที่หน้า Page3

    # องค์ประกอบในหน้าเมนู 1
    page.add(
        
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Page 1 Menu1 QR Code", size=30, weight=ft.FontWeight.BOLD),
                        ft.CircleAvatar(
                            foreground_image_url="https://via.placeholder.com/100",
                            radius=30,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Row([
                            ft.Image(src="https://picsum.photos/150/150?1", width=200, height=200),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,    
                        ),
                
                
                ft.NavigationBar(
                    destinations=[
                        ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                        ft.NavigationDestination(icon=ft.icons.CAR_RENTAL, label="Page1"),
                        ft.NavigationDestination(icon=ft.icons.GROUP, label="Page2"),
                        ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile"),
                    ],
                    selected_index=1,  # ตั้งค่าให้เลือก Page1
                    on_change=on_nav_change  # เพิ่ม callback เพื่อเปลี่ยนหน้า
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )
    


# ฟังก์ชันที่สร้างหน้าเมนู 2
def menu2_page(page):
    # ตั้งค่าหน้าเมนู 1
    page.title = "หน้ารายละเอียด 2"
    page.clean()  # ลบองค์ประกอบเก่าทั้งหมด
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ฟังก์ชันเมื่อมีการคลิกเปลี่ยนหน้าใน NavigationBar
        # ฟังก์ชันเมื่อมีการคลิกเปลี่ยนหน้าใน NavigationBar
    def on_nav_change(e):
        if e.control.selected_index == 0:
            home_page(page)  # กลับไปที่หน้า Home
        elif e.control.selected_index == 1:
            menu1_page(page)  # ไปที่หน้า Page1
        elif e.control.selected_index == 2:
            menu2_page(page)  # ไปที่หน้า Page2
        elif e.control.selected_index == 3:
            menu3_page(page)  # ไปที่หน้า Page3

    # องค์ประกอบในหน้าเมนู 1
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Page 2 Menu 2 ", size=30, weight=ft.FontWeight.BOLD), ft.CircleAvatar(
                                                                                                       foreground_image_url="https://via.placeholder.com/100",
                                                                                                       radius=30,
                                                                                                      )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Text("เพิ่มงานของท่านวันนี้"),
                ft.Image(src="https://picsum.photos/150/150?2", width=200, height=200),
                
                ft.NavigationBar(
                    destinations=[
                        ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                        ft.NavigationDestination(icon=ft.icons.CAR_RENTAL, label="Page1"),
                        ft.NavigationDestination(icon=ft.icons.GROUP, label="Page2"),
                        ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile"),
                    ],
                    selected_index=2,  # ตั้งค่าให้เลือก Page1
                    on_change=on_nav_change  # เพิ่ม callback เพื่อเปลี่ยนหน้า
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )


# ฟังก์ชันที่สร้างหน้าเมนู 3
def menu3_page(page):
    # ตั้งค่าหน้าเมนู 1
    page.title = "หน้ารายละเอียด 3"
    page.clean()  # ลบองค์ประกอบเก่าทั้งหมด
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ฟังก์ชันเมื่อมีการคลิกเปลี่ยนหน้าใน NavigationBar
        # ฟังก์ชันเมื่อมีการคลิกเปลี่ยนหน้าใน NavigationBar
    def on_nav_change(e):
        if e.control.selected_index == 0:
            home_page(page)  # กลับไปที่หน้า Home
        elif e.control.selected_index == 1:
            menu1_page(page)  # ไปที่หน้า Page1
        elif e.control.selected_index == 2:
            menu2_page(page)  # ไปที่หน้า Page2
        elif e.control.selected_index == 3:
            menu3_page(page)  # ไปที่หน้า Page3

    # องค์ประกอบในหน้าเมนู 3
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Page 3 Menu 3 Profile", size=30, weight=ft.FontWeight.BOLD),
                        ft.CircleAvatar(
                            foreground_image_url="https://via.placeholder.com/100",
                            radius=30,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),

                ft.Row([
                            ft.Image(src="https://picsum.photos/150/150?3", width=200, height=200),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,    
                ),

                ft.NavigationBar(
                    destinations=[
                        ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                        ft.NavigationDestination(icon=ft.icons.CAR_RENTAL, label="Page1"),
                        ft.NavigationDestination(icon=ft.icons.GROUP, label="Page2"),
                        ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile"),
                    ],
                    selected_index=3,  # ตั้งค่าให้เลือก Page1
                    on_change=on_nav_change  # เพิ่ม callback เพื่อเปลี่ยนหน้า
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )


# ฟังก์ชันที่สร้างหน้า Login
def login_page(page: ft.Page):
    def on_login_click(e):
        # ตรวจสอบการล็อกอิน
        if username_field.value == "a" and password_field.value == "123":
            # เรียกหน้า Home Page เมื่อเข้าสู่ระบบสำเร็จ
            home_page(page)
        else:
            # แสดงข้อความแจ้งเตือนเมื่อเข้าสู่ระบบไม่สำเร็จ
            page.add(ft.Text("Invalid username or password", color="red"))

    # องค์ประกอบหน้าจอล็อกอิน
    login_title = ft.Text("Login Page", size=30, weight=ft.FontWeight.BOLD)
    logo_image = ft.Image(src="https://via.placeholder.com/100", width=100, height=100)
    username_field = ft.TextField(label="Username", hint_text="Enter your username")
    password_field = ft.TextField(label="Password", hint_text="Enter your password", password=True)
    
    login_button = ft.ElevatedButton(text="Login", width=150, on_click=on_login_click)
    forgot_button = ft.ElevatedButton(text="Forgot Username", width=150)

    # จัดเรียงปุ่มในแนวนอน
    buttons_row = ft.Row([login_button, forgot_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    # เพิ่มองค์ประกอบทั้งหมดไปที่หน้าหลัก
    page.add(
        ft.Column(
            [
                login_title,
                logo_image,
                username_field,
                password_field,
                buttons_row,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

# ฟังก์ชันหลักที่เรียกหน้า login
def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    login_page(page)

# เรียกแอปพลิเคชัน
ft.app(target=main)
