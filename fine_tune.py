from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd

def fine_tune_model(data_path):
    model_name = "Narrativa/mT5-base-finetuned-tydiQA-question-generation"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    df = pd.read_csv(data_path)
    train_data = [
        {"text": text, "question": question}
        for text, question in zip(df['text'], df['question'])
    ]
    train_dataset = Dataset.from_list(train_data)

    def tokenize_function(examples):
        inputs = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=512)
        outputs = tokenizer(examples["question"], padding="max_length", truncation=True, max_length=64)
        return {
            "input_ids": inputs.input_ids,
            "attention_mask": inputs.attention_mask,
            "labels": outputs.input_ids,
        }

    tokenized_dataset = train_dataset.map(tokenize_function, batched=True)

    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()

    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")

if __name__ == "__main__":
    fine_tune_model("training_data.csv")