def reverse_string(user_input: str ) -> str:
  '''
  a function that reverse the entire input
  
  Args:
      user_input: str
  return:
        str: the reversed string of the input

   Raises:
        TypeError: If user_input is  not a string.

  Examples"
  >>> reverse_string('Karime')
  'emirak'
  >>> reverse_string('')
  ''
  >>> reverse_string('Mahdia')
  'aidhaM'


  '''
  assert(isinstance(user_input,str),TypeError("text must be a string"))
  
  reverse_str=''
  for chars in user_input:
    reverse_str = chars+reverse_str
  return reverse_str
     
