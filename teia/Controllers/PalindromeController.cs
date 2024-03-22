using Microsoft.AspNetCore.Mvc;
using System.Linq;

namespace PalindromeApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class PalindromeController : ControllerBase
    {
        [HttpPost]
        public IActionResult Post([FromBody] InputModel input)
        {
            var response = new
            {
                Palindromo = IsPalindrome(input.Texto),
                OcorrenciasCaracteres = GetCharacterOccurrences(input.Texto)
            };

            return Ok(response);
        }

        private bool IsPalindrome(string word)
        {
            int start = 0;
            int end = word.Length - 1;
            while (start < end)
            {
                if (char.ToLower(word[start]) != char.ToLower(word[end]))
                {
                    return false;
                }
                start++;
                end--;
            }
            return true;
        }

        private Dictionary<char, int> GetCharacterOccurrences(string input)
        {
            return input.GroupBy(c => c).ToDictionary(grp => grp.Key, grp => grp.Count());
        }

        public class InputModel
        {
            public string Texto { get; set; }
        }
    }
}
