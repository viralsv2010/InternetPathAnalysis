while(true)
do

        now=$(date +"%m_%d_%Y")

        echo "*****************       Ping    Command     Output ************************************" >> data_$now.txt

        echo "----------------------------------------------------------------------------------------" >> data_$now.txt

        echo "$(date)" >> data_$now.txt

        echo "----------------------------------------------------------------------------------------" >> data_$now.txt

        ping PL1.ENG.MONASH.EDU.AU -c 20 >> data_$now.txt

        echo "========================================================================================" >> data_$now.txt

        echo "========================================================================================" >> data_$now.txt

        echo "*****************   TraceRoute   Command     Output ************************************" >> data_trace_$now.txt

        echo "----------------------------------------------------------------------------------------" >> data_trace_$now.txt

        echo "$(date)" >> data_trace_$now.txt

        echo "----------------------------------------------------------------------------------------" >> data_trace_$now.txt

        traceroute PL1.ENG.MONASH.EDU.AU >> data_trace_$now.txt

        echo "========================================================================================" >> data_trace_$now.txt

        echo "========================================================================================" >> data_trace_$now.txt

        sleep 1h
done
