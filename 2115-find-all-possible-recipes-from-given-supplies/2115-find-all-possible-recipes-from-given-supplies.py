class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        food = defaultdict(list)
        indegree = defaultdict(int)
        res = []
        
        for r in range(len(recipes)):
            recipe = recipes[r]
            for i in ingredients[r]:
                food[i].append(recipe)
                indegree[recipe] += 1
        
        queue = deque(supplies)
        
        while queue:
            i = queue.popleft()
            
            for r in food[i]:
                indegree[r] -= 1
                
                if not indegree[r]:
                    queue.append(r)
                    
                    if r in recipes:
                        res.append(r)
        return res 
        

        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         food = defaultdict(list)
#         indegree = defaultdict(int)
#         res = []
        
#         for i in range(len(recipes)):
#             recipe = recipes[i]
#             for ingredient in ingredients[i]:
#                 food[ingredient].append(recipe)
#                 indegree[recipe] += 1
                
#         queue = deque(supplies)
#         while queue:
#             ingredient = queue.popleft()
#             for recipe in food[ingredient]:
#                 indegree[recipe] -= 1
                
#                 if not indegree[recipe]:
#                     queue.append(recipe)
#                     if recipe in recipes:
#                         res.append(recipe)
#         return res
            
            
            
    
        
        
        
        