import flet as ft


def main(page):
    page.title = "BMI calculator"
    page.horizontal_alignment = "center"
    
    def calculate_bmi(e):
        height = float(fld_height.value)
        weight = float(fld_weight.value)
        bmi = weight / (height/100)**2
        
        if bmi <= 18.5:  
            bmi_output = "Oops! You are underweight."
        elif bmi <= 24.9:  
            bmi_output = "Awesome! You are healthy."
        elif bmi <= 29.9:  
            bmi_output="Eee! You are over weight."
        else:  
            bmi_output="Seesh! You are obese."
        
        dlg = ft.AlertDialog(title=ft.Text(bmi_output))
        page.dialog = dlg
        dlg.open = True
        page.update()

    def reset(e):
        fld_height.value = ""
        fld_weight.value = ""
        page.update()
    
    txt_heading = ft.Text("BMI Calculator",size=35, weight=ft.FontWeight.W_900)
    fld_height = ft.TextField(label="your height in cm")
    fld_weight = ft.TextField(label="Your weight in kg")

    
    button_group=ft.Row(
                [
                    ft.FilledButton("Submit", on_click=calculate_bmi),
                    ft.ElevatedButton("Clear", on_click=reset,style=ft.ButtonStyle(bgcolor={"": ft.colors.RED},color={"":ft.colors.WHITE}))
                ],
                alignment="center"
            )
    
    page.add(txt_heading,fld_height,fld_weight,button_group)
    
ft.app(port=50001, target=main, view=ft.WEB_BROWSER)
