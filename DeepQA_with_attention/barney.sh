rm -rf save/model/* data/samples/*
cp save/FINAL_barney_model_30_epochs/* save/model
cp data/FINAL_barney_data_samples/* data/samples
python3 main.py --test interactive
