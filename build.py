import re,subprocess
s=open('src/CalligatorApp.jsx').read()
s=re.sub(r'^import React.*?;\n','',s,count=1,flags=re.M)
s='const { useState, useEffect, useRef, useMemo, useCallback } = React;\n'+s.replace('export default function CalligatorApp','function CalligatorApp',1)
s+='\nReactDOM.createRoot(document.getElementById("root")).render(<CalligatorApp />);\nif("serviceWorker" in navigator && location.protocol==="https:"){navigator.serviceWorker.register("/sw.js").catch(()=>{});}\n'
open('/tmp/entry.jsx','w').write(s)
NM='node_modules'
js=subprocess.check_output([NM+'/.bin/esbuild','/tmp/entry.jsx','--loader:.jsx=jsx','--target=es2018','--minify','--log-level=warning']).decode().replace('</script','<\\/script')
r=open(NM+'/react/umd/react.production.min.js').read(); d=open(NM+'/react-dom/umd/react-dom.production.min.js').read()
open('index.html','w').write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#EFE7D2">
<meta name="description" content="Calligator — a study buddy for electronics fundamentals: Ohm's Law, resistor codes, Boolean algebra, K-maps, and more.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Calligator">
<link rel="manifest" href="/manifest.json">
<link rel="icon" href="/icon-192.png">
<link rel="apple-touch-icon" href="/icon-192.png">
<title>Calligator</title>
<script>{r}</script>
<script>{d}</script>
</head>
<body style="margin:0;background:#EFE7D2">
<div id="root"></div>
<script>
{js}
</script>
</body>
</html>
''')
print('built')
