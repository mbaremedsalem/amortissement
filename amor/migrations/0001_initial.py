# Generated by Django 5.0.3 on 2024-04-02 11:33

import amor.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prtcli',
            fields=[
                ('NOOPER', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('NUMSEQ', models.IntegerField()),
                ('EXPL', models.CharField(max_length=100)),
                ('DATMAJ', models.DateField(blank=True, null=True)),
                ('EXPLMAJ', models.CharField(blank=True, max_length=100, null=True)),
                ('VALIDE', models.CharField(max_length=1)),
                ('DATJOUR', models.DateField()),
                ('DATOPER', models.DateField()),
                ('DATDERNC', models.DateField(blank=True, null=True)),
                ('CLIPRT', models.CharField(max_length=100)),
                ('DEVPRT', models.CharField(blank=True, max_length=100, null=True)),
                ('NCGPRT', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTPRT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTPRT', models.CharField(blank=True, max_length=100, null=True)),
                ('DATDEP', models.DateField(blank=True, null=True)),
                ('DATRMB', models.DateField(blank=True, null=True)),
                ('TYPIND', models.CharField(blank=True, max_length=100, null=True)),
                ('TXDB', models.CharField(blank=True, max_length=100, null=True)),
                ('TXDBAN', models.CharField(blank=True, max_length=100, null=True)),
                ('NJANDB', models.CharField(blank=True, max_length=100, null=True)),
                ('PERRMB', models.CharField(blank=True, max_length=100, null=True)),
                ('PERINT', models.CharField(blank=True, max_length=100, null=True)),
                ('TYPCALC', models.CharField(blank=True, max_length=100, null=True)),
                ('TYPRMB', models.CharField(blank=True, max_length=100, null=True)),
                ('NOOPREC', models.CharField(blank=True, max_length=100, null=True)),
                ('XCOMDEC', models.CharField(blank=True, max_length=100, null=True)),
                ('DERNRMB', models.CharField(blank=True, max_length=100, null=True)),
                ('TOTINT', models.CharField(blank=True, max_length=100, null=True)),
                ('DERNDAT', models.DateField(blank=True, null=True)),
                ('TOTRMB', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTVUE', models.CharField(blank=True, max_length=100, null=True)),
                ('MODRMB', models.CharField(blank=True, max_length=100, null=True)),
                ('INTDIF', models.CharField(blank=True, max_length=100, null=True)),
                ('MODASS', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTASS', models.CharField(blank=True, max_length=100, null=True)),
                ('TXASS', models.CharField(blank=True, max_length=100, null=True)),
                ('TXT1', models.CharField(blank=True, max_length=100, null=True)),
                ('TXMIN', models.CharField(blank=True, max_length=100, null=True)),
                ('TXMAX', models.CharField(blank=True, max_length=100, null=True)),
                ('TXTAXE', models.CharField(blank=True, max_length=100, null=True)),
                ('MODDIF', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTDEB', models.CharField(blank=True, max_length=100, null=True)),
                ('XDOS', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTDOS', models.CharField(blank=True, max_length=100, null=True)),
                ('CVMNTDOS', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXDOS', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXDOS', models.CharField(blank=True, max_length=100, null=True)),
                ('CVMNTTAXDOS', models.CharField(blank=True, max_length=100, null=True)),
                ('TXASSINI', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTASF', models.CharField(blank=True, max_length=100, null=True)),
                ('TXFONGAR', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFONGAR', models.CharField(blank=True, max_length=100, null=True)),
                ('TXFONASS', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFONASS', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTNETCLI', models.CharField(blank=True, max_length=100, null=True)),
                ('XRECALC', models.CharField(blank=True, max_length=100, null=True)),
                ('TYPTAUX', models.CharField(blank=True, max_length=100, null=True)),
                ('DATCONTR', models.DateField(blank=True, null=True)),
                ('TXTEG', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTCONTR', models.CharField(blank=True, max_length=100, null=True)),
                ('XRECALCD', models.CharField(blank=True, max_length=100, null=True)),
                ('DATRMBANT', models.DateField(blank=True, null=True)),
                ('MNTRESTDU', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTINTINT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXINT', models.CharField(blank=True, max_length=100, null=True)),
                ('TXPEN', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTPEN', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXPEN', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTRMBANT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTNEWPRT', models.CharField(blank=True, max_length=100, null=True)),
                ('TYPNEWPRT', models.CharField(blank=True, max_length=100, null=True)),
                ('NOPRTCSET', models.CharField(blank=True, max_length=100, null=True)),
                ('OPER', models.CharField(blank=True, max_length=100, null=True)),
                ('CSERV', models.CharField(blank=True, max_length=100, null=True)),
                ('CNSIGN', models.CharField(blank=True, max_length=100, null=True)),
                ('NSIGN', models.CharField(blank=True, max_length=100, null=True)),
                ('PSIGN', models.CharField(blank=True, max_length=100, null=True)),
                ('TOTSIGN', models.CharField(blank=True, max_length=100, null=True)),
                ('PSIGN11', models.CharField(blank=True, max_length=100, null=True)),
                ('EXPLV1', models.CharField(blank=True, max_length=100, null=True)),
                ('EXPLV2', models.CharField(blank=True, max_length=100, null=True)),
                ('EXPLV3', models.CharField(blank=True, max_length=100, null=True)),
                ('XPOSOPER', models.CharField(blank=True, max_length=100, null=True)),
                ('STATE', models.CharField(blank=True, max_length=100, null=True)),
                ('CVMNTDEP', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTAUT1', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTAUT2', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTAUT3', models.CharField(blank=True, max_length=100, null=True)),
                ('CODDCIC', models.CharField(blank=True, max_length=100, null=True)),
                ('EXPLCI', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTINIFGV', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTPERFGV', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTECH1', models.CharField(blank=True, max_length=100, null=True)),
                ('PRCECH1', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTECH2', models.CharField(blank=True, max_length=100, null=True)),
                ('PRCECH2', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTECH3', models.CharField(blank=True, max_length=100, null=True)),
                ('PRCECH3', models.CharField(blank=True, max_length=100, null=True)),
                ('DATRMBFM', models.DateField(blank=True, null=True)),
                ('CLASSIF', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTAUTH', models.CharField(blank=True, max_length=100, null=True)),
                ('DEPASS', models.CharField(blank=True, max_length=100, null=True)),
                ('CRSYNDIQ', models.CharField(blank=True, max_length=100, null=True)),
                ('XNOREVDIFF', models.CharField(blank=True, max_length=100, null=True)),
                ('DATPREMREVTX', models.DateField(blank=True, null=True)),
                ('MANDATAIRE', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFONGAR', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFONGAR', models.CharField(blank=True, max_length=100, null=True)),
                ('CVMNTTAXFONGAR', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFONASS', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFONASS', models.CharField(blank=True, max_length=100, null=True)),
                ('CVMNTTAXFONASS', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTVENT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTACH', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTACPT', models.CharField(blank=True, max_length=100, null=True)),
                ('PXREV', models.CharField(blank=True, max_length=100, null=True)),
                ('TXPRFTS', models.CharField(blank=True, max_length=100, null=True)),
                ('RMBFRAIS', models.CharField(blank=True, max_length=100, null=True)),
                ('RMBTAXE', models.CharField(blank=True, max_length=100, null=True)),
                ('RMBPRFT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTPRFTS', models.CharField(blank=True, max_length=100, null=True)),
                ('XMODIFTX', models.CharField(blank=True, max_length=100, null=True)),
                ('BIENDESC1', models.CharField(blank=True, max_length=100, null=True)),
                ('BIENDESC2', models.CharField(blank=True, max_length=100, null=True)),
                ('TAUXTIMBRE', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTIMBRE', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTPRFTRES', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTPRFTPAY', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTMOB', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTMOBREV', models.CharField(blank=True, max_length=100, null=True)),
                ('DATMAJMOB', models.DateField(blank=True, null=True)),
                ('EXPLMAJMOB', models.CharField(blank=True, max_length=100, null=True)),
                ('XMOBILISABLE', models.CharField(blank=True, max_length=100, null=True)),
                ('BIENDESC3', models.CharField(blank=True, max_length=100, null=True)),
                ('BIENDESC4', models.CharField(blank=True, max_length=100, null=True)),
                ('BIENDESC', models.CharField(blank=True, max_length=100, null=True)),
                ('REFREL', models.CharField(blank=True, max_length=100, null=True)),
                ('RMBTIMBRE', models.CharField(blank=True, max_length=100, null=True)),
                ('TAUXFRAISDIV', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFRAISDIV', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFRAISDIV', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFRAISDIV', models.CharField(blank=True, max_length=100, null=True)),
                ('CVMNTTAXFRAISDIV', models.CharField(blank=True, max_length=100, null=True)),
                ('RMBFRAISDIV', models.CharField(blank=True, max_length=100, null=True)),
                ('RMBTAXFRAISDIV', models.CharField(blank=True, max_length=100, null=True)),
                ('CHEFFILE', models.CharField(blank=True, max_length=100, null=True)),
                ('BICAGENT', models.CharField(blank=True, max_length=100, null=True)),
                ('NUMTIR', models.CharField(blank=True, max_length=100, null=True)),
                ('NOOPERTIR', models.CharField(blank=True, max_length=100, null=True)),
                ('OBJOPERATION', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFRMENS', models.CharField(blank=True, max_length=100, null=True)),
                ('NOOPERPAR', models.CharField(blank=True, max_length=100, null=True)),
                ('NETOFF', models.CharField(blank=True, max_length=100, null=True)),
                ('REFINANCE', models.CharField(blank=True, max_length=100, null=True)),
                ('MOTIFREFINANCE', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXASF', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXASF', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTDEBLOC', models.CharField(blank=True, max_length=100, null=True)),
                ('TXDEBLOC', models.CharField(blank=True, max_length=100, null=True)),
                ('XDEBLOCAGEMULTIPLE', models.CharField(blank=True, max_length=100, null=True)),
                ('TAXASS', models.CharField(blank=True, max_length=100, null=True)),
                ('TXDEBLOCMARGE', models.CharField(blank=True, max_length=100, null=True)),
                ('TYPIJARA', models.CharField(blank=True, max_length=100, null=True)),
                ('TRANSFERTITLE', models.CharField(blank=True, max_length=100, null=True)),
                ('CODANN', models.CharField(blank=True, max_length=100, null=True)),
                ('RESANN', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTOKEN', models.CharField(blank=True, max_length=100, null=True)),
                ('NOOPTRADING', models.CharField(blank=True, max_length=100, null=True)),
                ('CODMINDEP', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTHB', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTSALE', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTEFFECTEDBANKASSET', models.CharField(blank=True, max_length=100, null=True)),
                ('ASSETTYPE', models.CharField(blank=True, max_length=100, null=True)),
                ('ACTION', models.CharField(blank=True, max_length=100, null=True)),
                ('PREVVALSEQ', models.CharField(blank=True, max_length=100, null=True)),
                ('XDEFERREDPERIODICITY', models.CharField(blank=True, max_length=100, null=True)),
                ('DEFERREDPERIODICITY', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTIMPRMBANT', models.CharField(blank=True, max_length=100, null=True)),
                ('CVMNTDEPCLI', models.CharField(blank=True, max_length=100, null=True)),
                ('XPOSOPERCLI', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTCAPCAP', models.CharField(blank=True, max_length=100, null=True)),
                ('SYND_AGCODE', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTIMPINT', models.CharField(blank=True, max_length=100, null=True)),
                ('CONVENTION', models.CharField(blank=True, max_length=100, null=True)),
                ('TITRE_LAIUS', models.CharField(blank=True, max_length=100, null=True)),
                ('XSIGNE', models.CharField(blank=True, max_length=100, null=True)),
                ('DEDUCTTOTUNEARNFROMHIBA', models.CharField(blank=True, max_length=100, null=True)),
                ('SUMMNTRMBANT_UNEARNED', models.CharField(blank=True, max_length=100, null=True)),
                ('DATRMBDIFF', models.DateField(blank=True, null=True)),
                ('PERINTPAY', models.CharField(blank=True, max_length=100, null=True)),
                ('RENOVACIOO', models.CharField(blank=True, max_length=100, null=True)),
                ('TRACKREF', models.CharField(blank=True, max_length=100, null=True)),
                ('LATE_FEE_TYPCALC', models.CharField(blank=True, max_length=100, null=True)),
                ('MOTIF', models.CharField(blank=True, max_length=100, null=True)),
                ('NOOPERCONT', models.CharField(blank=True, max_length=100, null=True)),
                ('MODIF_CDR', models.CharField(blank=True, max_length=100, null=True)),
                ('XAMORT_MANUEL', models.CharField(blank=True, max_length=100, null=True)),
                ('MODCALCINT', models.CharField(blank=True, max_length=100, null=True)),
                ('XLOCKOUT', models.CharField(blank=True, max_length=100, null=True)),
                ('NBJLOCKOUT', models.CharField(blank=True, max_length=100, null=True)),
                ('INDFLOOR', models.CharField(blank=True, max_length=100, null=True)),
                ('VALINDFLOOR', models.CharField(blank=True, max_length=100, null=True)),
                ('CAS', models.CharField(blank=True, max_length=100, null=True)),
                ('XTXTAXESPECIAL', models.CharField(blank=True, max_length=100, null=True)),
                ('XREVOLVE', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTHBK2D', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTHBK2C', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTHBREVD', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTHBREVC', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTHBCAPD', models.CharField(blank=True, max_length=100, null=True)),
                ('CPTHBCAPC', models.CharField(blank=True, max_length=100, null=True)),
                ('TYPINDIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('TXDBIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('COEDBIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTINTIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTINTIMPTAX', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTMRGIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTMRGIMPTAX', models.CharField(blank=True, max_length=100, null=True)),
                ('LOOKBACK', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTINTIMPINT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTINTIMPINTTAX', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTMRGIMPINT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTMRGIMPINTTAX', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFRSIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFRSIMPTAX', models.CharField(blank=True, max_length=100, null=True)),
                ('BASMRGIMP', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR2COMMENT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR2DATEFF', models.DateField(blank=True, null=True)),
                ('MNTFR2PER', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFR2', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR2', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR4DATEFF', models.DateField(blank=True, null=True)),
                ('MNTFR4PER', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFR4', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR4', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR5COMMENT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR5DATEFF', models.DateField(blank=True, null=True)),
                ('MNTFR5PER', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFR5', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR5', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR1COMMENT', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR1DATEFF', models.DateField(blank=True, null=True)),
                ('MNTFR1PER', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFR1', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR1', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR3', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTTAXFR3', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR3PER', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR3DATEFF', models.DateField(blank=True, null=True)),
                ('MNTFR4COMMENT', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFRAIS5', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFRAIS3', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFRAIS4', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFRAIS2', models.CharField(blank=True, max_length=100, null=True)),
                ('XTAXFRAIS1', models.CharField(blank=True, max_length=100, null=True)),
                ('NOOPERSUBCONT', models.CharField(blank=True, max_length=100, null=True)),
                ('XFORBEARANCE', models.CharField(blank=True, max_length=100, null=True)),
                ('FORBEARANCEMOTIF', models.CharField(blank=True, max_length=100, null=True)),
                ('FORBEARANCEDATDEP', models.DateField(blank=True, null=True)),
                ('DATSIGN', models.DateField(blank=True, null=True)),
                ('TXTAXPEN', models.CharField(blank=True, max_length=100, null=True)),
                ('MNTFR3COMMENT', models.CharField(blank=True, max_length=100, null=True)),
                ('XSKIPJOURFERIE', models.CharField(blank=True, max_length=100, null=True)),
                ('DATRMBORIG', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prtcli',
            },
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nom', models.CharField(blank=True, max_length=50)),
                ('prenom', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=16, unique=True)),
                ('username', models.CharField(max_length=16, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=amor.models.image_uoload_profile)),
                ('is_active', models.BooleanField(default=True)),
                ('verified', models.BooleanField(default=False)),
                ('restricted', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('number_attempt', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset_password_token', models.CharField(blank=True, default='', max_length=50)),
                ('reset_password_expire', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
