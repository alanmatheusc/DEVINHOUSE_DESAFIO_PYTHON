def timeConversion(s):
  horario = int(s[0:2])
  manha = s.endswith('AM')
  tarde = s.endswith('PM')
  if(tarde and horario != 12):
    horario += 12
    return s.replace(s[0:2],str(horario)).replace("PM","")
  elif(tarde and horario == 12):
    return s.replace("PM","")
  elif(manha and horario == 12):
    return s.replace(s[0:2],"00").replace("AM","")
  else:
    return s.replace("AM","")
timeConversion("12:45:54PM")