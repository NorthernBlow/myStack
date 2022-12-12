print ("Hello world")


-- factorialis n! (эн факториал)

function fact(n)
	if n==0 then
		return 1

	else 
		return n*fact(n-1)
	end

end

print ("enter a number:")

a = io.read("*n")  --считывает число и записывает в переменную a

print(fact(a))



--пример хвостового вызова функции
function tail(n)
  print "function tail in action"
  if n>0 then return tail(n-1) end
end

tail(10)