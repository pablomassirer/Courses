#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);

int count_words(string text);

int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    // Letter, Word and Sentence Quantities respective variables.
    int letter_qtt = count_letters(text);
    int word_qtt = count_words(text);
    int sentence_qtt = count_sentences(text);
    float L = (float)letter_qtt / word_qtt * 100;
    float S = (float)sentence_qtt / word_qtt * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    index = round(index);
    // Verifies if is less than 1, otherwise verifies if is greather than 16, else compares grade (index)
    // with every iteration until finds it in a 16 range loop.
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        for (int i = 0; i < 16; i++)
        {
            if (i == index)
            {
                printf("Grade %i\n", i);
            }
        }
    }
}

int count_letters(string text)
{
    int count = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(string text)
{
    int count = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isspace(text[i]))
        {
            count++;
        }
    }
    return count + 1;
}

int count_sentences(string text)
{
    int count = 0;
    bool hasContent;
    for (int i = 0, len = strlen(text); i < len; i++)
    { // Check if string starts with alpha content in every iteration, to avoid only punctuation or void data.
        if (isalpha(text[i]))
        {
            hasContent = true;
        }
        if ((text[i] == '!' || text[i] == '?' || text[i] == '.') && (hasContent))
        {
            hasContent = false;
            count++;
        }
    }
    return count;
}