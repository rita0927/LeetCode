class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        food = defaultdict(list)
        indegree = defaultdict(int)
        res = []
        recipe_set = set(recipes)
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                food[ingredient].append(recipe)
                indegree[recipe] += 1
                
        queue = deque(supplies)
        while queue:
            ingredient = queue.popleft()
            for recipe in food[ingredient]:
                indegree[recipe] -= 1
                
                if not indegree[recipe]:
                    queue.append(recipe)
                    if recipe in recipe_set:
                        res.append(recipe)
        return res
            
            
            
    
        
        
        
        