def calcular_frequencia():
    try:
        dias_frequentados = int(entry_dias_frequentados.get())
        dias_letivos = int(entry_dias_letivos.get())
        frequencia = (dias_frequentados * 100) / dias_letivos
        messagebox.showinfo("Resultado", f"A frequência do aluno é {frequencia:.2f}%")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Frequência do Aluno")

# Definir o tamanho da janela e centralizá-la na tela
largura_janela = 400
altura_janela = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Criação dos widgets
label_dias_frequentados = tk.Label(janela, text="Dias Frequentados:", font=("Helvetica", 14))
label_dias_frequentados.pack(pady=10)

entry_dias_frequentados = tk.Entry(janela, font=("Helvetica", 14))
entry_dias_frequentados.pack(pady=10)

label_dias_letivos = tk.Label(janela, text="Dias Letivos:", font=("Helvetica", 14))
label_dias_letivos.pack(pady=10)

entry_dias_letivos = tk.Entry(janela, font=("Helvetica", 14))
entry_dias_letivos.pack(pady=10)

botao_calcular = tk.Button(janela, text="Calcular Frequência", command=calcular_frequencia, font=("Helvetica", 14))
botao_calcular.pack(pady=20)

# Iniciar o loop principal da interface gráfica
janela.mainloop()