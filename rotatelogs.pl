#!/usr/bin/perl

my $path = '/home/hduser/smp/logs';
@fnames = `ls -1 $path/Backup.MIFEngine.*.log.gz $path/Backup.IngestionEngine.*.log.gz`;

foreach $fname (@fnames)
{
    chomp($fname);
    $basename = `basename $fname`;
    ($Backup, $logname, $timestamp, $log, $gz) = split('\.', $basename);
    print $basename;
    $timestamp = substr($timestamp, 0, -2);
    if ( ! -d "$path/$timestamp")
        {
            `mkdir $path/$timestamp`;
        }
print "Copy $fname to $path/$timestamp/$basename\n";
`cp $fname $path/$timestamp/$basename`;
}
