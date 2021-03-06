=begin
 *
 * autor Maurício Freire
 * Calcula o fatorial de um número.
 * Calculates the fatorial of a number.
=end

def fatorial(n)
    if n == 1 
        return 1
    end
    return n * fatorial(n - 1)
end

n = gets.chomp.to_i
puts "#{n}! = #{fatorial(n)}"
