=begin

  @autor Maurício Freire
  Mostra a representação binária de um dado número.
  Shows the binary representation of a chosen number.
=end

print "Digite um número: "
n = gets.chomp.to_i
bin = []

# Converte o número digitado para 0 e 1.
# Convertes the typed number to 0 and 1.
print "#{n} em binário é: "
for i in 15.downto(0)
    if n % 2 == 0
        bin[i] = 0
    else
        bin[i] = 1
    end
    n = n / 2
end

# Exibe a representação binária do número.
# Shows the binary representation of the number.
for i in 0..15
    if i % 8 == 0
        print " "
    end
    print bin[i]
end
