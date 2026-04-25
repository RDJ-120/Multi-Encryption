import argparse
import hashlib
import base64
from hmac import new
from rich import traceback
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress
from rich.markdown import Markdown
from rich.theme import Theme
import re
import unicodedata
	
MORSE_EN = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
                'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
                'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
                'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----',
                '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
                '7':'--...','8':'---..','9':'----.',' ':'/'}
MORSE_AR = {'ا':'.-','ب':'-...','ت':'-.-.','ث':'-..','ج':'.','ح':'..-.','خ':'--.',
                'د':'....','ذ':'..','ر':'.---','ز':'-.-','س':'.-..','ش':'--','ص':'-.',
                'ض':'---','ط':'.--.','ظ':'--.-','ع':'.-.','غ':'...','ف':'-','ق':'..-',
                'ك':'...-','ل':'.--','م':'-..-','ن':'-.--','ه':'--..','و':'.--.-','ي':'-.--.',' ':'/'}
                
c_t = Theme(
		{"info": "bold cyan", "regular": "bold green", "error": "bold red"})
traceback.install()
c = Console(theme=c_t)
layout = Layout()

parser = argparse.ArgumentParser(description="Hashing, base64 De-Encoder and Morse De-Encoder Tool")

sub = parser.add_subparsers(dest="cmd", required=True)

hash = sub.add_parser("hash")
hash.add_argument("type", help="Hash Type", choices=["sha256", "md5", "sha512", "sha1"])
hash.add_argument("text", help="Text To Hash")


base = sub.add_parser("base64")

g = base.add_mutually_exclusive_group(required=True)

g.add_argument("-e", "--encode", help="Base64 Encoder", action="store_true")

g.add_argument("-d", "--decode", help="Base64 Decoder", action="store_true")

base.add_argument("text", help="Text To Decode Or Encode")

hmac = sub.add_parser("hmac")

hmac.add_argument("-k" ,"--key", help="Key To Use In Hashing", required=True)

hmac.add_argument("-t" ,"--text", help="Text To Use In Hashing", required=True)

hmac.add_argument("-ty","--type", help="Type To Hash With", required=True)

morse = sub.add_parser("morse")

gg = morse.add_mutually_exclusive_group(required=True)

gg.add_argument("-a", "--arabic", help="Morse Arabic", action="store_true")

gg.add_argument("-e", "--english", help="Morse English", action="store_true")

morse.add_argument("text", help="Text To Encode Or Decode")

mode = morse.add_mutually_exclusive_group(required=True)

mode.add_argument("-en", "--encode", help="Encoding With Morse", action="store_true")

mode.add_argument("-de", "--decode", help="Decoding With Morse", action="store_true")

args = parser.parse_args()
ARABIC_DIACRITICS = re.compile(r'[\u064B-\u0652]')
def normalize_arabic(s):
    s = ARABIC_DIACRITICS.sub('', s)
    s = s.replace('ـ','').replace('أ','ا').replace('إ','ا').replace('آ','ا')
    s = s.replace('ة','ه').replace('ى','ي').replace('ؤ','و').replace('ئ','ي').replace('ء','')
    for i,ch in enumerate('٠١٢٣٤٥٦٧٨٩'): s = s.replace(ch,str(i))
    return unicodedata.normalize('NFC',s)
  
  
  
if args.cmd == "hash":
	if args.type == "sha256":
		hashed = hashlib.sha256(args.text.encode("utf-8")).hexdigest()
		c.print(Panel(
		f"[info]{hashed}",
		title="[regular]Hashing Result",
		style="bold green on black")
		)
		
	elif args.type == "sha512":
		hashed = hashlib.sha512(args.text.encode("utf-8")).hexdigest()
		c.print(Panel(
		f"[info]{hashed}",
		title="[regular]Hashing Result",
		style="bold green on black")
		)
		
	elif args.type == "md5":
		hashed = hashlib.md5(args.text.encode("utf-8")).hexdigest()
		c.print(Panel(
		f"[info]{hashed}",
		title="[regular]Hashing Result",
		style="bold green on black")
		)
		
	elif args.type == "sha1":
		hashed = hashlib.sha1(args.text.encode("utf-8")).hexdigest()
		c.print(Panel(
		f"[info]{hashed}",
		title="[regular]Hashing Result",
		style="bold green on black")
		)
	
	
if args.cmd == "base64":
	if args.encode:
		text = args.text
		text = text.encode("utf-8")
		based = base64.b64encode(text).decode("utf-8")
		c.print(Panel(
		f"[info]{based}",
		title="[regular]Encoding Result",
		style="bold green on black"))
		
	elif args.decode:
		text = args.text
		text = text.encode("utf-8")
		based = base64.b64decode(text).decode("utf-8")
		c.print(Panel(
		f"[info]{based}",
		title="[regular]Decoding Result",
		style="bold green on black"))


elif args.cmd == "hmac":
	text = args.text.encode("utf-8")
	key = args.key.encode("utf-8")
	type = args.type
	
	if type == "sha256":
		hashed = new(key, text, hashlib.sha256).hexdigest()
		
	elif type == "sha512":
		hashed = new(key, text, hashlib.sha512).hexdigest()
		
	elif type == "sha1":
		hashed = new(key, text, hashlib.sha1).hexdigest()
		
	elif type == "md5":
		hashed = new(key, text, hashlib.md5).hexdigest()
		
	else:
		hashed = "Invaild Type"
		
	c.print(Panel(
		f"[info]{hashed}",
		title="[regular]Hashing Result",
		style="bold green on black")
		)


if args.cmd == "morse":
	result = []
	if args.arabic:
		dict = MORSE_AR
		if args.encode:
			text = normalize_arabic(args.text)
			for letter in text:
				result.append(dict.get(letter, ''))
			text = " ".join(result)
			c.print(Panel(	f"[regular]Result:\n[info]{text}\n\n[regular]Language:	[info]Arabic",
		title="[regular]Encoding Result",
		style="bold green on black"))
		elif args.decode:
			text = args.text
			rev = {v:k for k,v in MORSE_AR.items()}
			parts = re.findall(r"\S+", text)
			final = ""
			for part in parts:
				if part == "/":
					final += " "
				else:
					final += rev.get(part, "")
			c.print(Panel(	f"[regular]Result:\n[info]{final}\n\n[regular]Language:	[info]Arabic",
		title="[regular]Decoding Result",
		style="bold green on black"))
				
	elif args.english:
		dict = MORSE_EN
		if args.encode:
			text = args.text
			for letter in text.upper():
				result.append(dict.get(letter, ''))
			text = " ".join(result)
			c.print(Panel(
	f"[regular]Result:\n[info]{text}\n\n[regular]Language:\t[info]English",
    title="[regular]Encoding Result",
    style="bold green on black"
	))
			
		elif args.decode:
			text = args.text
			rev = {v:k for k,v in MORSE_EN.items()}
			parts = re.findall(r"\S+", text)
			final = ""
			for part in parts:
				if part == "/":
					final += " "
				else:
					final += rev.get(part, "")
			c.print(Panel(
  f"[regular]Result:\n[info]{text}\n\n[regular]Language:\t[info]English",
    title="[regular]Decoding Result",
    style="bold green on black"
))
