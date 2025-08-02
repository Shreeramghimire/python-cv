from fpdf import FPDF
import yaml

def generate_cv():
    with open("cv_config.yaml") as f:
        data = yaml.safe_load(f)
    
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=24)
    pdf.cell(0, 10, data["name"], ln=True)
    
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, data["title"], ln=True)
    
    
    pdf.output("my_cv.pdf")

if __name__ == "__main__":
    generate_cv()