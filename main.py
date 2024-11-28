import yt_dlp

def baixar_audio_mp3(link, nome_arquivo="audio_baixado.mp3"):
    try:
        # Configuração para baixar apenas o áudio
        ydl_opts = {
            'format': 'bestaudio/best',  # Melhor formato de áudio
            'outtmpl': nome_arquivo,    # Nome do arquivo de saída
            'postprocessors': [{        # Converte para MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  # Qualidade do áudio em kbps
            }],
        }

        # Baixar o áudio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando áudio de {link}...")
            ydl.download([link])
        print(f"Áudio salvo como {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao baixar áudio: {e}")

# Exemplo de uso
link_youtube = "https://www.youtube.com/watch?v=Ryp134JrCSk"
baixar_audio_mp3(link_youtube)
