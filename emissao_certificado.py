import openpyxl
from PIL import Image, ImageDraw, ImageFont

nomes_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
pag_alunos = nomes_alunos['Sheet1']

for index, linha in enumerate(pag_alunos.iter_rows(min_row=2)):
    nome_curso = linha[0].value
    aluno = linha[1].value
    tipo_participante = linha[2].value
    data_inicio = linha[3].value
    data_terminio = linha[4].value
    carga_horaria = linha[5].value
    emissao = linha[6].value

    fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)
    fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)
    fonte_hora = ImageFont.truetype('./tahoma.ttf', 50)

    imagem = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(imagem)

    desenhar.text((1050, 825), aluno, fill='black', font=fonte_nome)
    desenhar.text((1090, 950), nome_curso, fill='black', font=fonte_geral)
    desenhar.text((1450,1068), tipo_participante, fill='black', font=fonte_geral)
    desenhar.text((1500, 1188), str(carga_horaria), fill='black', font=fonte_geral)

    desenhar.text((760,1785), str(data_inicio), fill='red', font=fonte_hora)
    desenhar.text((760,1945), str(data_terminio), fill='red', font=fonte_hora)
    desenhar.text((2235,1940), str(emissao), fill='red', font=fonte_hora)

    imagem.save(f'./Certificados/{index} - {aluno} certificado.png')
