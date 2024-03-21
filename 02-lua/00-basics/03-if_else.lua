-- Branching in Lua
level = 1
num_lives = 5
score = 0
time_elapsed = 0

-- TODO: the game starts
if score >= 1000 then -- IF-ELSE STATEMENT
    level = level + 1
    num_lives = 5
else
time_elapsed = time_elapsed + 1
end

print("Level: " .. level)
print("Score: " .. score)
print("Lives: " .. num_lives)
print("Time Elapsed: " .. time_elapsed)

