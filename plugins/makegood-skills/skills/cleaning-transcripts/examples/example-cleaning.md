# Example: cleaning a raw dictation transcript

This shows a short raw transcript, the cleaned result, and the uncertain-corrections report that would accompany it in the chat response.

---

## Raw transcript (input)

```
[Speaker 1]
Okay so, um, today I want to, I want to walk through the, the onboarding flow for.

[Speaker 1]
For new customers. So right now when somebody signs up they hit the, the welcome
screen and then, uh, they get dropped into what we call the, the sand box. Um.

[Speaker 1]
And the problem is, is that a lot of them, you know, they, they don't really know
what to do next. So we saw, like, a 30. A 30 percent drop off right at that point.
Um, and we think if we add a, a guided tour using apend do, that we can, we can
cut that in half.
```

## Cleaned transcript (deliverable)

> Okay, so today I want to walk through the onboarding flow for new customers. Right now, when somebody signs up they hit the welcome screen, and then they get dropped into what we call the sandbox.
>
> And the problem is that a lot of them don't really know what to do next. So we saw about a 30 percent drop-off right at that point. We think that if we add a guided tour using Appcues, we can cut that in half.

## Uncertain-corrections report (in the chat response, not in the file)

> One correction to confirm:
>
> - **"apend do" → "Appcues"** — the transcription is garbled here; from context ("a guided tour"), this is almost certainly a product-onboarding tool, and Appcues is the most likely match. Please confirm the tool name, since I'm inferring it.
>
> Everything else was filler removal ("um," "uh," "you know," and the repeated-word stutters), joining the fragmented lines into paragraphs, and "sand box" → "sandbox." Your wording, order, the 30 percent figure, and the "cut that in half" point are all preserved as spoken.
