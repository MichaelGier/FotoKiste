fotokisteCfg = {}

fotokisteCfg['window-width']    = 1280
fotokisteCfg['window-height']   = 1024

# Depending on the camera used previews might got smaller than set here
fotokisteCfg['cam-p-width']     = 960
fotokisteCfg['cam-p-height']    = 720
fotokisteCfg['cam-p-x']         = 9
fotokisteCfg['cam-p-y']         = 261
fotokisteCfg['cam-p-hflip']     = True # False = Like a camera, True = Like a mirror

# PiCam v1: 2592x1944, v2: 3280x2464
fotokisteCfg['cam-c-width']     = 3280
fotokisteCfg['cam-c-height']    = 2464
fotokisteCfg['cam-c-hflip']     = False # False = Like a camera, True = Like a mirror

fotokisteCfg['nopi']            = False #True = Skip rasperry specific modules

fotokisteCfg['temp']            = '/tmp/fotokiste/'
fotokisteCfg['save']            = '/home/pi/fotokiste/images/'

fotokisteCfg['countdown']       = 3 # Seconds

fotokisteText = {}

fotokisteText['info-home']    = 'Hallo und willkommen in der fotokiste!<br>Drücke einfach auf &quot;Aufnahme&quot; und los geht es!'
fotokisteText['info-count']   = 'Los geht es!<hr><span style="font-size: 200%; font-weight: bolder;">${countdown}</span>'
fotokisteText['info-capture'] = '<span style="font-size: 200%; font-weight: bolder;">Bitte lächeln!</span>'
fotokisteText['info-review']  = 'Alles OK?<br>Wenn ja drücke auf "Speichern". Doch zu blöd geguckt? Dann versuch es gleich nochmal.'
fotokisteText['info-view']    = 'Hier kannst du dir die Fotos der Veranstaltung direkt anschauen. Mit "Nächstes" und "Vorheriges" kannst du zwischen den Bildern wechseln. Mit "Zurück" geht es wieder zur Kamera.'

fotokisteText['btn-capture']  = 'Aufnahme ▶'
fotokisteText['btn-view']     = 'Ansehen ▶'
fotokisteText['btn-save']     = 'Speichern ▶'
fotokisteText['btn-recapture'] = '<span style="font-size: 75%">Neuer Versuch</span> ▶'
fotokisteText['btn-cancel']   = 'Abbruch ▶'
fotokisteText['btn-next']     = 'Nächstes ▶'
fotokisteText['btn-previous'] = 'Vorheriges ▶'
fotokisteText['btn-back']     = 'Zurück ▶'
fotokisteText['btn-empty']    = ''