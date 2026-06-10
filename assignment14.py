import gc 
import sys 
 
class Node: 
    def __init__(self, name): 
        self.name = name 
        self.link = None 
 
    def __del__(self): 
        print(f"{self.name} is being destroyed") 
 
 
gc.disable() 
 
print("========== Creating Nodes ==========\n") 
 
A = Node("Node A") 
B = Node("Node B") 
 
A.link = B 
B.link = A 
 
print("Cycle created:") 
print("A -> B") 
print("B -> A\n") 
 
print("========== Reference Counts ==========\n") 
 
print("Reference count of A:", sys.getrefcount(A)) 
print("Reference count of B:", sys.getrefcount(B)) 
 
print("\n========== Deleting References ==========\n") 
 
del A 
del B 
 
print("Variables A and B deleted") 
print("Objects still exist because of cyclic references\n") 
 
print("========== Checking Garbage Collector ==========\n") 
 
unreachable_before = len(gc.garbage) 
 
print("Unreachable objects before collection:", unreachable_before) 
print("\n========== Forcing Garbage Collection ==========\n") 
collected = gc.collect() 
print("Unreachable objects collected:", collected) 
unreachable_after = len(gc.garbage) 
print("Unreachable objects after collection:", unreachable_after) 
print("\n========== Program Finished ==========")