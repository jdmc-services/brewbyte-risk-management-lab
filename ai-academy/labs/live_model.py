"""Optional genuine model execution; no hosted API. Never run downloaded remote code."""
import argparse
import json
import time


def generate(model_id, revision, text):
    from transformers import pipeline
    from brewbyte import validate_text, scrub
    text = scrub(validate_text(text))
    start = time.perf_counter()
    generator = pipeline('text-generation', model=model_id, revision=revision,
                         trust_remote_code=False, device=-1)
    output = generator(text, max_new_tokens=64, do_sample=False, return_full_text=False)
    return {'backend': 'local-transformers', 'model': model_id, 'revision': revision,
            'generated_text': output[0]['generated_text'], 'seconds_including_load': time.perf_counter()-start,
            'limits': 'Small models can fail instructions. Evaluate actual outputs; never execute them.'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model', required=True, help='Instructor-approved model ID')
    p.add_argument('--revision', required=True, help='Reviewed model commit/revision')
    p.add_argument('--text', default='BrewByte Coffee serves tea. Write one short factual summary:')
    a = p.parse_args()
    print(json.dumps(generate(a.model, a.revision, a.text), indent=2))
