import config
from config import PerFL


class Arguments:
    def __init__(self):
        self.pgd = True
        self.detector = 6  # 2 means norm bound, 1 means krum and 0 nothing, 3 is GAN-based, 4 means opt_armor
        self.attack = 2  # 1 means random sampling, 3 means single shots 5 means no attack, 4 means model replacement
        self.single_shot_round = 30
        self.attackers_list = [0]
        self.enable_detector = False
        self.attack_step = 1
        self.attakType = 1  # 1 means data poisoning
        self.start_round = 0
        self.eps = 2.2  # parameter of pgd
        self.sigma = 0.025
        self.diffPrivacy = True
        self.bound = 5
        self.log_name = "newGANMNIST_updated_.csv"
        self.epsilon = 8
        self.delta = 10 ** (-5)
        self.n_batch = 3
        self.N_LOTS = 3
        self.batch_size = 16
        self.gan_loss_th1 = 0.11
        self.gan_loss_th2 = 0.11
        self.opt_loss_th = 100
        self.latent_size = 64
        self.hidden_size = 256
        self.image_size = 784
        self.max_iterations_opt = 300
        self.max_loss_opt = 2
        self.max_retries = 2
        self.ignore_detection_th = 10
        self.model_to_load = "train_model_84.pt"  # "model_attack_.pt"#"./model_35.pt"
        self.savemodel = 10
        ###############################

        self.test_batch_size = 64
        self.beta1 = 0.5
        self.no_cuda = False
        self.seed = 0
        self.log_interval = 10
        self.outf = '.'
        self.save_model = True
        self.path = 'train_model'
        #############################
        self.gpu = True
        self.num_users = 10
        self.iid = True
        self.unequal = True
        self.dataset = 'texas'
        self.classifier = 'vgg'
        self.fc_hidden_sizes = [1024, 512, 256, 128]
        self.num_channels = 1
        self.num_classes = 32
        self.epochs = 1
        self.frac = 1
        self.local_bs = 5
        self.local_ep = 5
        self.lr = 0.001
        self.momentum = 0.5
        self.criterion = 'cross_entropy'
        self.optimizer = 'adam'
        self.verbose = 1
        self.attacker_index = 0

        self.measure_layer_latent_information = True
        self.normalize_jacobian_norm = False

        self.ganepochs = 100
        self.ganBatchSize = 128
        self.g_step = 1
        self.d_step = 1
        self.load_state_dict = False

        self.nbdt = False
        self.sdt = False

        # Attack
        self.train_target_model = False
        self.train_shadow_model = False
        self.train_attack_model = False
        self.need_augm = True
        self.need_topk = False
        self.verbose = True
        self.param_init = True
        self.model_path = 'train_model_86.pt'
        self.data_path = './data'
        self.attack_directory = './attack_model'
        self.attack_min_epoch = 290

        # Motionsense Path
        self.motionsense_train_path = './data/motionsense/train'
        self.motionsense_test_path = './data/motionsense/test'

        # Protection Mechanism
        self.ppm = "wdp"
        self.shared_aggregation = False
        self.shared_aggregation_rate = 0.5
        self.perfl_layers = ["classifier"]
        self.layer_type = "linear"

        # Data results
        self.result_path = f'./results/analysis_purchase_by_layer_tests.csv'

        #Relaxloss
        self.relaxloss_alpha = 0.2

        self.posterior_flattening = False
        self.posterior_flattening_epoch = 0

        # SDT
        self.feature_size = 16000

        self.prob_distribution = None

        self.E = 1

        self.tot_T = 1
        self.clip = 5
