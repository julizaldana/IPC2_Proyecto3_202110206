from fpdf import FPDF

class PDF(FPDF):
    pass
    def texts(self,name):
        with open(name,'rb') as xy:
            txt = xy.read().decode('latin-1')
            self.set_xy(10.0,80.0)
            self.set_text_color(76.0,32.0,250.0)
            self.set_font('Arial', '', 12)
            self.multi_cell(0,10,txt)

    def titles(self,title):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220,50,50)
        self.cell(w=210.0, h=40.0, align='C', txt=title, border=0)


