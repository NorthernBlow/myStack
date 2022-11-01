-- Двоичный поиск — классический алгоритм поиска элемента в отсортированном массиве, 
-- использующий дробление массива на половины. Используется в информатике,
-- вычислительной математике и математическом программировании.


local modulee = {}

function modulee.binary_search(list, item)
  local low = 0
  local high = #list
  
  while low <= high do
    local mid = (low + high)
    local guess = list[mid]
    
    if guess == item then
      return mid
      end
    if guess > item then
      high = mid -1
    else
      low = mid + 1
      end
  return nil
end
return modulee
      end
