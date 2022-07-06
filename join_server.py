import requests
import time
davet_linki = 'https://discord.gg/WQErwe'
real_invite = 'https://discordapp.com/api/v6/invite/' + davet_linki.split('/')[-1]

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

log('Program başladı.')
log('Yapımcı: Can')
log('GitHub: https://github.com/fastuptime')
with open('tokens.txt', 'r', encoding='utf-8') as f:
    tokens = f.read()
    tokens = tokens.split('\n')
    for token in tokens:
        headers = {
            'Authorization': token
        }
        log(token + ' tokeni davet ediliyor...')
        try:
            r = requests.post(real_invite, headers=headers)
            if r.status_code == 200:
                log(token + ' tokeni davet edildi.')
            else:
                log(token + ' tokeni davet edilemedi.')
            time.sleep(3)
        except:
            log(token + ' tokeni davet edilemedi.')
            time.sleep(3)
                