Procedure to evaluate the performance of RCR ciphers using the SUPERCOP toolkit
-------------------------------------------------------------------------------
1. Download the latest SUPERCOP from https://bench.cr.yp.to/supercop.html and unpack it.
2. Unpack RCR_supercop.tar and copy the folders rcr32, rcr64, rcr32secure and rcr64secure into the SUPERCOP stream cipher directory supercop-<version>/crypto_stream/.
3. Run the following commands:
	cd supercop-<version>/
	sh do-part crypto_stream rcr32
	cat  ./bench/localhost/data >> ../data_rcr
    sh do-part crypto_stream rcr64
    cat  ./bench/localhost/data >> ../data_rcr
	sh do-part crypto_stream rcr32secure
	cat  ./bench/localhost/data >> ../data_rcr
    sh do-part crypto_stream rcr64secure
    cat  ./bench/localhost/data >> ../data_rcr
4. Run the following command to extract the encryption timings for all message sizes:
	cd ..
	python3 super_analyse_1.py  > rcr_timings
5. Run the following command to extract the performance in cycles per byte to encrypt 64-byte, 576-byte, 1536-byte, 4096-byte and long messages.
     cd ..
     python3 super_analyse_2.py  > rcr_cycles
