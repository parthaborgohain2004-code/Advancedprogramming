class ScoreProcessor: 
 
    def process_score_file(self, file_path: str) -> int: 
 
        try: 
            with open(file_path, "r") as file: 
                content = file.read().strip() 
 
                score = int(content) 
 
                result = score * 10 
 
        except FileNotFoundError: 
            print("Error: File not found.") 
            raise 
 
        except ValueError: 
            print("Error: Invalid number format in file.") 
            raise 
 
        else: 
            print("Data processed successfully") 
            return result 
 
        finally: 
            print("File cleanup completed")