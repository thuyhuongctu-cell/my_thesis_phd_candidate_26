import re
import unicodedata
import Levenshtein

HTML_TAG = re.compile(r'<.*?>')

class TitleMatcher:
    # Common mathematical symbol replacements
    MATH_SYMBOL_MAP = {
        '$\\mathcal{A}$': 'A',
        '$\\alpha$': 'alpha',
        '$\\beta$': 'beta',
        '$\\lambda$': 'lambda',
        '$\\Omega$': 'Omega',
        '∈': 'in',
        '≠': 'not equal',
        '≤': 'less than or equal',
        '≥': 'greater than or equal',
        # Add more as needed
    }

    STOP_WORDS = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'with'}

    @staticmethod
    def preprocess_math_symbols(title: str) -> str:
        """Replace mathematical symbols with their text equivalents."""
        processed_title = title
        for symbol, replacement in TitleMatcher.MATH_SYMBOL_MAP.items():
            processed_title = processed_title.replace(symbol, replacement)
        return processed_title

    @staticmethod
    def normalize_title(title: str) -> str:
        """Title normalization that removes all hyphens and em dashes."""
        # First, handle math symbols
        title = TitleMatcher.preprocess_math_symbols(title)
        
        # Normalize Unicode characters
        title = unicodedata.normalize('NFKD', title)
        
        # remove all non-ASCII characters and math symbols
        title = ''.join(char for char in title if ord(char) < 128 or not TitleMatcher.ismath(char))
        
        # Convert to lowercase
        title = title.lower()
        
        # remove tags if any
        title = re.sub(HTML_TAG, '', title)
        
        # Replace em dashes with spaces (to avoid words getting joined)
        title = title.replace('—', ' ')
        
        # Remove all special characters including hyphens
        title = re.sub(r'[^\w\s]', '', title)
        
        # Remove stop words
        words = title.split()
        filtered_words = [word for word in words if word not in TitleMatcher.STOP_WORDS]
        
        # Sort words to handle word order differences
        filtered_words.sort()
        
        return ' '.join(filtered_words)
    
    @staticmethod
    def ismath(char: str) -> bool:
        """Check if a character is a Unicode math character."""
        return unicodedata.category(char).startswith('So') and \
               (ord(char) >= 0x1D400 and ord(char) <= 0x1D7FF)

    @staticmethod
    def calculate_similarity(title1: str, title2: str) -> float:
        """Calculate similarity using Levenshtein distance."""
        norm_title1 = TitleMatcher.normalize_title(title1)
        norm_title2 = TitleMatcher.normalize_title(title2)
        
        max_len = max(len(norm_title1), len(norm_title2))
        if max_len == 0:
            return 1.0
        
        distance = Levenshtein.distance(norm_title1, norm_title2)
        return 1 - (distance / max_len)