# Sample Test Data for AI Study Buddy

## 📚 Test Examples for Markers

Here are sample study notes you can use to test the AI flashcard generation:

### Example 1: Computer Science - Algorithms
```
Big O notation is used to describe the performance or complexity of an algorithm. 
O(1) describes constant time complexity - the algorithm will always execute in the same time regardless of input size.
O(n) describes linear time complexity - the execution time increases linearly with input size.
O(n²) describes quadratic time complexity - common with nested loops.
Binary search has O(log n) complexity because it divides the search space in half each iteration.
```

### Example 2: Biology - Cell Biology
```
Mitochondria are known as the powerhouse of the cell because they produce ATP through cellular respiration.
The cell membrane is selectively permeable, controlling what enters and exits the cell.
Ribosomes are responsible for protein synthesis and can be found free-floating or attached to the endoplasmic reticulum.
DNA is stored in the nucleus and contains the genetic instructions for cellular functions.
Photosynthesis occurs in chloroplasts and converts light energy into chemical energy.
```

### Example 3: History - World War II
```
World War II began on September 1, 1939, when Germany invaded Poland.
The Holocaust was the systematic persecution and murder of six million Jews by Nazi Germany.
D-Day occurred on June 6, 1944, when Allied forces launched the largest seaborne invasion in history at Normandy.
The atomic bombs were dropped on Hiroshima (August 6) and Nagasaki (August 9) in 1945.
The war ended on September 2, 1945, with Japan's formal surrender.
```

### Example 4: Chemistry - Periodic Table
```
Elements in the periodic table are arranged by atomic number.
Groups are vertical columns that contain elements with similar properties.
Periods are horizontal rows representing electron shells.
Noble gases are in Group 18 and are chemically inert.
Alkali metals in Group 1 are highly reactive and form ionic compounds readily.
```

## 🧪 How to Test

1. **Go to the live app**: `https://your-app-name.onrender.com/ui`
2. **Copy any example above** into the text area
3. **Click "Generate 5 Quiz Questions"**
4. **Wait for AI processing** (may take 10-30 seconds)
5. **Review generated flashcards** - they should be relevant to the input
6. **Test flashcard functionality** - click to flip cards
7. **Check persistence** - refresh page and click "View Previous Flashcards"

## ✅ Expected Results

- **5 unique questions** generated from the input text
- **Questions should be relevant** to the subject matter
- **Answers should be accurate** based on the provided notes
- **Flashcards should flip** when clicked (CSS animation)
- **Questions should persist** in database and appear in "Previous" tab

## 🎯 Evaluation Criteria

- **AI Integration**: Does the app successfully generate questions using AI?
- **Database Functionality**: Are flashcards saved and retrievable?
- **User Interface**: Is the design clean and functional?
- **Responsiveness**: Does it work on different screen sizes?
- **Error Handling**: How does it handle invalid input or API failures?

---
**Note**: First load may take 30-60 seconds due to Render free tier cold start.
