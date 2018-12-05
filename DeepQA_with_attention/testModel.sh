if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    echo "Please state one of either {generic, spock, vader, barney}"
    exit 1
fi

rm -rf save/model/* data/samples/*
echo "Removed samples and model"
cp save/FINAL_$1_model_30_epochs/* save/model
echo "Copied model weights over"
cp data/FINAL_$1_data_samples/* data/samples
echo "Copied samples over"
python3 main.py --test interactive
