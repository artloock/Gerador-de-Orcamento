#call fpdf.
from fpdf import FPDF

#request values.
Project = input('Project description: ')
project_est_time = input('Project estimated time: ')
hour_value = input('Hour time value: ')
deliver_date = input('Estimate deliveri time: ')

#sum total value
total_value = int(project_est_time)*int(hour_value)

#generate PDF file whit template
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial')

pdf.image("template.png",x=0, y=0)

pdf.text(115, 145, Project)
pdf.text(115, 160, project_est_time)
pdf.text(115, 175, hour_value)
pdf.text(115, 190, deliver_date)
pdf.text(115, 205, str(total_value))

pdf.output('Orçamento.pdf')

#print text
print('Orçamento gerado com sucesso!')